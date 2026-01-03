// Contribute.js - KreyolAPI Contribution System

// Configuration
const API_BASE_URL = 'https://api.kreyolapi.org'; // Change this to your actual API URL
const EMAIL_ENDPOINT = `${API_BASE_URL}/send-contribution`; // Email endpoint

// State management
let currentDirection = 'en-ht';
let currentDomain = 'general';
let contributionCount = 0;

// DOM Elements
const directionButtons = document.querySelectorAll('.direction-btn');
const domainRadios = document.querySelectorAll('input[name="domain"]');
const contributionForm = document.getElementById('contributionForm');
const contributorName = document.getElementById('contributorName');
const sourceText = document.getElementById('sourceText');
const targetText = document.getElementById('targetText');
const context = document.getElementById('context');
const submitBtn = document.getElementById('submitBtn');
const btnText = submitBtn.querySelector('.btn-text');
const btnLoader = submitBtn.querySelector('.btn-loader');
const successMessage = document.getElementById('successMessage');
const errorMessage = document.getElementById('errorMessage');
const addAnotherBtn = document.getElementById('addAnotherBtn');
const sourceLanguageLabel = document.getElementById('sourceLanguageLabel');
const targetLanguageLabel = document.getElementById('targetLanguageLabel');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  setupEventListeners();
  updateLanguageLabels();
  generateContributionId();
});

// Generate unique contribution ID
function generateContributionId() {
  contributionCount++;
  const timestamp = Date.now();
  return `contrib_${timestamp}_${contributionCount}`;
}

// Event Listeners
function setupEventListeners() {
  // Direction buttons
  directionButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      directionButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentDirection = btn.dataset.direction;
      updateLanguageLabels();
    });
  });

  // Domain selection
  domainRadios.forEach(radio => {
    radio.addEventListener('change', (e) => {
      currentDomain = e.target.value;
    });
  });

  // Form submission
  contributionForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    await handleContribution();
  });

  // Add another contribution
  addAnotherBtn.addEventListener('click', () => {
    resetForm();
  });
}

// Update language labels based on direction
function updateLanguageLabels() {
  const [source, target] = currentDirection.split('-');
  
  // Get translation function from language switcher
  const t = window.KreyolAPI ? window.KreyolAPI.t : (key) => key;
  
  if (source === 'en') {
    sourceLanguageLabel.textContent = t('contribute.source.label.en');
    targetLanguageLabel.textContent = t('contribute.target.label.ht');
    sourceText.placeholder = t('contribute.source.placeholder.en');
    targetText.placeholder = t('contribute.target.placeholder.ht');
  } else {
    sourceLanguageLabel.textContent = t('contribute.source.label.ht');
    targetLanguageLabel.textContent = t('contribute.target.label.en');
    sourceText.placeholder = t('contribute.source.placeholder.ht');
    targetText.placeholder = t('contribute.target.placeholder.en');
  }
}

// Handle contribution submission
async function handleContribution() {
  // Validate form
  if (!sourceText.value.trim() || !targetText.value.trim()) {
    alert('Please fill in both the source text and translation.');
    return;
  }

  // Disable button and show loading
  submitBtn.disabled = true;
  btnText.style.display = 'none';
  btnLoader.style.display = 'inline';
  errorMessage.style.display = 'none';

  try {
    // Prepare contribution data
    const [source_lang, target_lang] = currentDirection.split('-');
    const contributionData = formatContributionData(source_lang, target_lang);
    
    // Send to backend
    const response = await fetch(EMAIL_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(contributionData)
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Show success message
    showSuccess();
    
  } catch (error) {
    console.error('Contribution submission error:', error);
    showError();
  } finally {
    // Re-enable button
    submitBtn.disabled = false;
    btnText.style.display = 'inline';
    btnLoader.style.display = 'none';
  }
}

// Format contribution data for CSV format
function formatContributionData(source_lang, target_lang) {
  const id = generateContributionId();
  const name = contributorName.value.trim() || 'Anonymous';
  const additionalContext = context.value.trim();
  
  // Create CSV-formatted data
  const csvRow = {
    id: id,
    source_language: source_lang,
    target_language: target_lang,
    source: sourceText.value.trim(),
    target: targetText.value.trim(),
    domain: currentDomain
  };
  
  // Create detailed note for email
  const contributionNote = `
=================================================================
NEW TRANSLATION CONTRIBUTION
=================================================================

Contribution ID: ${id}
Contributor Name: ${name}
Date: ${new Date().toLocaleString()}
Domain: ${currentDomain}

-----------------------------------------------------------------
CSV FORMAT (Ready to add to dataset):
-----------------------------------------------------------------
${id},${source_lang},${target_lang},"${escapeCSV(sourceText.value.trim())}","${escapeCSV(targetText.value.trim())}",${currentDomain}

-----------------------------------------------------------------
DETAILED INFORMATION:
-----------------------------------------------------------------
Source Language: ${source_lang.toUpperCase()}
Target Language: ${target_lang.toUpperCase()}
Domain: ${currentDomain.toUpperCase()}

Source Text (${source_lang}):
${sourceText.value.trim()}

Translation (${target_lang}):
${targetText.value.trim()}

${additionalContext ? `Additional Context:\n${additionalContext}\n` : ''}
-----------------------------------------------------------------
CONTRIBUTOR INFORMATION:
-----------------------------------------------------------------
Name: ${name}
Submission Time: ${new Date().toISOString()}

=================================================================
`;

  return {
    to_email: 'psechein@gmail.com',
    subject: `[KreyolAPI] New Contribution: ${source_lang}→${target_lang} - ${currentDomain}`,
    contribution_note: contributionNote,
    csv_data: csvRow,
    contributor_name: name
  };
}

// Escape CSV special characters
function escapeCSV(text) {
  // Replace double quotes with two double quotes for CSV format
  return text.replace(/"/g, '""');
}

// Show success message
function showSuccess() {
  // Hide form fields
  const formGroups = document.querySelectorAll('.form-group');
  formGroups.forEach(group => {
    group.style.display = 'none';
  });
  submitBtn.style.display = 'none';
  
  // Show success message
  successMessage.style.display = 'block';
  
  // Scroll to success message
  successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Show error message
function showError() {
  errorMessage.style.display = 'block';
  
  // Hide error after 5 seconds
  setTimeout(() => {
    errorMessage.style.display = 'none';
  }, 5000);
}

// Reset form
function resetForm() {
  // Show form fields again
  const formGroups = document.querySelectorAll('.form-group');
  formGroups.forEach(group => {
    group.style.display = 'block';
  });
  submitBtn.style.display = 'block';
  
  // Hide success message
  successMessage.style.display = 'none';
  
  // Clear form
  contributionForm.reset();
  contributorName.value = '';
  sourceText.value = '';
  targetText.value = '';
  context.value = '';
  
  // Reset to default direction
  directionButtons.forEach(btn => btn.classList.remove('active'));
  directionButtons[0].classList.add('active');
  currentDirection = 'en-ht';
  updateLanguageLabels();
  
  // Reset domain to general
  currentDomain = 'general';
  document.querySelector('input[value="general"]').checked = true;
  
  // Scroll to top of form
  contributionForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

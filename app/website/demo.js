// Demo.js - KreyolAPI Interactive Demo

// Configuration
const API_BASE_URL = 'https://api.kreyolapi.org'; // Change this to your actual API URL

// State management
let currentDirection = 'en-ht';
let currentDomain = 'general';
let lastTranslation = null;

// DOM Elements
const directionButtons = document.querySelectorAll('.direction-btn');
const domainRadios = document.querySelectorAll('input[name="domain"]');
const sourceText = document.getElementById('sourceText');
const charCount = document.getElementById('charCount');
const translationForm = document.getElementById('translationForm');
const translateBtn = document.getElementById('translateBtn');
const btnText = translateBtn.querySelector('.btn-text');
const btnLoader = translateBtn.querySelector('.btn-loader');
const outputSection = document.getElementById('outputSection');
const translationOutput = document.getElementById('translationOutput');
const sourceLanguageLabel = document.getElementById('sourceLanguageLabel');
const targetLanguageLabel = document.getElementById('targetLanguageLabel');
const confidenceBadge = document.getElementById('confidenceBadge');
const warningsSection = document.getElementById('warningsSection');
const warningsList = document.getElementById('warningsList');
const feedbackSection = document.getElementById('feedbackSection');
const feedbackButtons = document.querySelectorAll('.feedback-btn');
const feedbackComment = document.getElementById('feedbackComment');
const feedbackText = document.getElementById('feedbackText');
const submitFeedbackBtn = document.getElementById('submitFeedback');
const feedbackThanks = document.getElementById('feedbackThanks');
const exampleButtons = document.querySelectorAll('.example-btn');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  setupEventListeners();
  updateLanguageLabels();
});

// Event Listeners
function setupEventListeners() {
  // Direction buttons
  directionButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      directionButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentDirection = btn.dataset.direction;
      updateLanguageLabels();
      clearOutput();
    });
  });

  // Domain selection
  domainRadios.forEach(radio => {
    radio.addEventListener('change', (e) => {
      currentDomain = e.target.value;
      clearOutput();
    });
  });

  // Character counter
  sourceText.addEventListener('input', () => {
    const length = sourceText.value.length;
    charCount.textContent = `${length} / 500`;
  });

  // Form submission
  translationForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    await handleTranslation();
  });

  // Example buttons
  exampleButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const text = btn.dataset.text;
      const lang = btn.dataset.lang;
      
      // Set the correct direction
      const targetDirection = lang === 'en' ? 'en-ht' : 'ht-en';
      if (currentDirection !== targetDirection) {
        const targetBtn = document.querySelector(`[data-direction="${targetDirection}"]`);
        targetBtn.click();
      }
      
      sourceText.value = text;
      charCount.textContent = `${text.length} / 500`;
      sourceText.focus();
    });
  });

  // Feedback buttons
  feedbackButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const feedbackType = btn.dataset.feedback;
      
      if (feedbackType === 'helpful') {
        showFeedbackThanks();
        logFeedback('positive', null);
      } else {
        feedbackComment.style.display = 'block';
        feedbackText.focus();
      }
    });
  });

  // Submit feedback
  submitFeedbackBtn.addEventListener('click', () => {
    const comment = feedbackText.value.trim();
    logFeedback('negative', comment);
    showFeedbackThanks();
  });
}

// Update language labels based on direction
function updateLanguageLabels() {
  const [source, target] = currentDirection.split('-');
  
  // Get translation function from language switcher
  const t = window.KreyolAPI ? window.KreyolAPI.t : (key) => key;
  
  if (source === 'en') {
    sourceLanguageLabel.textContent = t('demo.source.en');
    targetLanguageLabel.textContent = t('demo.target.ht');
    sourceText.placeholder = t('demo.placeholder.en');
  } else {
    sourceLanguageLabel.textContent = t('demo.source.ht');
    targetLanguageLabel.textContent = t('demo.target.en');
    sourceText.placeholder = t('demo.placeholder.ht');
  }
}

// Handle translation
async function handleTranslation() {
  const text = sourceText.value.trim();
  
  if (!text) {
    alert('Please enter some text to translate');
    return;
  }

  // Disable button and show loading
  translateBtn.disabled = true;
  btnText.style.display = 'none';
  btnLoader.style.display = 'inline';

  try {
    const [source, target] = currentDirection.split('-');
    
    const response = await fetch(`${API_BASE_URL}/v1/translate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text: text,
        source_language: source,
        target_language: target,
        domain: currentDomain
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    lastTranslation = data;
    displayTranslation(data);

  } catch (error) {
    console.error('Translation error:', error);
    alert('Translation failed. Please check your connection and try again.\n\nError: ' + error.message);
  } finally {
    // Re-enable button
    translateBtn.disabled = false;
    btnText.style.display = 'inline';
    btnLoader.style.display = 'none';
  }
}

// Display translation results
function displayTranslation(data) {
  // Show output section
  outputSection.style.display = 'block';
  
  // Display translation
  translationOutput.textContent = data.translation;
  
  // Display confidence
  displayConfidence(data.confidence);
  
  // Display warnings if any
  if (data.warnings && data.warnings.length > 0) {
    displayWarnings(data.warnings);
  } else {
    warningsSection.style.display = 'none';
  }
  
  // Show feedback section
  feedbackSection.style.display = 'block';
  feedbackComment.style.display = 'none';
  feedbackThanks.style.display = 'none';
  feedbackText.value = '';
  
  // Scroll to results
  outputSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Display confidence badge
function displayConfidence(confidence) {
  const t = window.KreyolAPI ? window.KreyolAPI.t : (key) => key;
  let badgeClass = '';
  let badgeText = '';
  
  if (confidence >= 0.9) {
    badgeClass = 'confidence-high';
    badgeText = `${t('demo.confidence.high')} (${Math.round(confidence * 100)}%)`;
  } else if (confidence >= 0.7) {
    badgeClass = 'confidence-medium';
    badgeText = `${t('demo.confidence.medium')} (${Math.round(confidence * 100)}%)`;
  } else {
    badgeClass = 'confidence-low';
    badgeText = `${t('demo.confidence.low')} (${Math.round(confidence * 100)}%)`;
  }
  
  confidenceBadge.className = `confidence-badge ${badgeClass}`;
  confidenceBadge.textContent = badgeText;
}

// Display warnings
function displayWarnings(warnings) {
  warningsSection.style.display = 'block';
  warningsList.innerHTML = '';
  
  const warningMessages = {
    'SIMPLIFIED_FOR_SAFETY': 'Translation was simplified for accuracy',
    'LOW_CONFIDENCE_SIMPLIFIED': 'Low confidence - simplified translation provided',
    'POTENTIAL_FRENCH_STRUCTURE': 'Potential French language structure detected',
    'FRENCH_GRAMMAR_PATTERN': 'French grammar patterns detected',
    'ENGLISH_VERB_LEAK': 'English verb patterns detected',
    'MISSING_TENSE_MARKER': 'Tense marker may be missing',
    'ARTICLE_POSITION_SUSPECT': 'Article position may need adjustment',
    'LONG_SENTENCE_POSSIBLE_AMBIGUITY': 'Long sentence - may have ambiguity'
  };
  
  warnings.forEach(warning => {
    const li = document.createElement('li');
    li.textContent = warningMessages[warning] || warning;
    warningsList.appendChild(li);
  });
}

// Clear output
function clearOutput() {
  outputSection.style.display = 'none';
  feedbackSection.style.display = 'none';
  lastTranslation = null;
}

// Show feedback thanks message
function showFeedbackThanks() {
  feedbackComment.style.display = 'none';
  feedbackThanks.style.display = 'block';
  
  // Hide after 3 seconds
  setTimeout(() => {
    feedbackSection.style.display = 'none';
  }, 3000);
}

// Log feedback and send via email
async function logFeedback(type, comment) {
  const feedback = {
    type: type,
    comment: comment,
    translation: lastTranslation,
    timestamp: new Date().toISOString()
  };
  
  console.log('Feedback logged:', feedback);
  
  // Send feedback to backend for email
  try {
    const response = await fetch(`${API_BASE_URL}/send-feedback`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        to_email: 'persona@gmail.com',
        subject: `[KreyolAPI] User Feedback - ${type}`,
        feedback_data: feedback
      })
    });
    
    if (!response.ok) {
      console.error('Failed to send feedback email');
    }
  } catch (error) {
    console.error('Error sending feedback:', error);
    // Don't show error to user - feedback is optional
  }
}

// Utility function to get readable warning names
function getWarningName(code) {
  const names = {
    'POTENTIAL_FRENCH_STRUCTURE': 'Potential French Structure',
    'LOW_CONFIDENCE_SIMPLIFIED': 'Low Confidence',
    'SIMPLIFIED_FOR_SAFETY': 'Simplified Translation',
    'FRENCH_GRAMMAR_PATTERN': 'French Grammar',
    'ENGLISH_VERB_LEAK': 'English Verb Pattern',
    'MISSING_TENSE_MARKER': 'Missing Tense Marker',
    'ARTICLE_POSITION_SUSPECT': 'Article Position',
    'LONG_SENTENCE_POSSIBLE_AMBIGUITY': 'Long Sentence'
  };
  
  return names[code] || code;
}
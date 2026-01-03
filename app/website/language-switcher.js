// language-switcher.js - Bilingual interface for Vokal Kreyòl

// Translation dictionary
const translations = {
  en: {
    // Navigation & Common
    'nav.home': 'Home',
    'nav.demo': 'Try Demo',
    'nav.contribute': 'Contribute',
    'nav.docs': 'API Docs',
    'nav.back': '← Back to Home',
    
    // Landing Page (index.html)
    'index.title': 'Vokal Kreyòl',
    'index.subtitle': 'Public, non-profit infrastructure for Haitian Creole language access',
    'index.tagline': 'Built for communities, education, journalism, healthcare, legal, technology  and public services.',
    'index.why.title': 'Why Vokal Kreyòl?',
    'index.why.text1': 'Haitian Creole is spoken by over 12 million people, yet it remains underrepresented in high-quality language infrastructure.',
    'index.why.text2': 'Vokal Kreyòl exists to provide accurate, transparent, and community-grounded translation services as a public good — not a commercial product.',
    'index.what.title': 'What We Provide',
    'index.what.item1': '📘 Haitian Creole ↔ English translation API',
    'index.what.item2': '🧠 Hybrid neural + dataset-based translation',
    'index.what.item3': '🌍 Open access for public-interest use',
    'index.what.item4': '🔎 Focus on linguistic accuracy and consistency',
    'index.api.title': 'API Usage',
    'index.api.note': 'No authentication required during the public pilot phase.',
    'index.who.title': 'Who Is This For?',
    'index.who.item1': 'Nonprofit organizations',
    'index.who.item2': 'Schools and educators',
    'index.who.item3': 'Journalists and media outlets',
    'index.who.item4': 'Developers building Creole-accessible tools',
    'index.who.item5': 'Public institutions',
    'index.ethics.title': 'Governance & Ethics',
    'index.ethics.text': 'KreyolAPI is a nonprofit public infrastructure project. We do not sell user data, and our goal is long-term community stewardship of Haitian Creole language technology.',
    'index.footer.rights': '© 2026 Vokal Kreyòl — Public Language Infrastructure',
    'index.footer.contact': 'Contact:',
    
    // Demo Page (demo.html)
    'demo.title': 'Try Vokal Kreyòl',
    'demo.subtitle': 'Experience accurate Haitian Creole translation',
    'demo.heading': 'Translation Demo',
    'demo.direction.label': 'Translation Direction:',
    'demo.direction.en-ht': 'English → Kreyòl',
    'demo.direction.ht-en': 'Kreyòl → English',
    'demo.domain.label': 'Domain:',
    'demo.domain.general': 'General',
    'demo.domain.healthcare': 'Healthcare',
    'demo.domain.education': 'Education',
    'demo.source.en': 'English Text',
    'demo.source.ht': 'Haitian Creole Text',
    'demo.target.en': 'English Translation',
    'demo.target.ht': 'Haitian Creole Translation',
    'demo.placeholder.en': 'Type or paste your text here...',
    'demo.placeholder.ht': 'Ekri oswa kole tèks ou a isit la...',
    'demo.chars': 'characters',
    'demo.translate.btn': 'Translate',
    'demo.translate.loading': 'Translating...',
    'demo.confidence.high': 'High confidence',
    'demo.confidence.medium': 'Medium confidence',
    'demo.confidence.low': 'Low confidence',
    'demo.warnings.title': '⚠️ Translation Notes:',
    'demo.feedback.question': 'Was this translation helpful?',
    'demo.feedback.yes': '👍 Yes, helpful',
    'demo.feedback.no': '👎 Needs improvement',
    'demo.feedback.placeholder': 'Optional: Tell us how we can improve this translation...',
    'demo.feedback.submit': 'Submit Feedback',
    'demo.feedback.thanks': '✅ Thank you for your feedback! It helps us improve Vokal Kreyòl.',
    'demo.examples.title': 'Try these examples:',
    'demo.api.title': 'Using Vokal Kreyòl in Your App',
    'demo.api.text': 'This demo uses the same API you can integrate into your applications:',
    'demo.api.link': 'View Full API Documentation →',
    
    // Contribute Page (contribute.html)
    'contribute.title': 'Contribute Translations',
    'contribute.subtitle': 'Help us build better Haitian Creole language tools',
    'contribute.description': 'Your contributions help improve translation quality for everyone. Share phrases, sentences, or terms you use in your daily life.',
    'contribute.heading': 'Add a New Translation',
    'contribute.instructions': 'Share a phrase or sentence and its translation. Your contribution will be reviewed and added to our dataset.',
    'contribute.name.label': 'Your Name',
    'contribute.name.optional': '(for reference)',
    'contribute.name.placeholder': 'Enter your name (optional)',
    'contribute.direction.label': "I'm contributing from:",
    'contribute.category.label': 'Category:',
    'contribute.source.label.en': 'English Text',
    'contribute.source.label.ht': 'Haitian Creole Text',
    'contribute.source.required': '*',
    'contribute.source.placeholder.en': 'Enter the text in English...',
    'contribute.source.placeholder.ht': 'Ekri tèks la an Kreyòl...',
    'contribute.source.hint': 'Enter a word, phrase, or sentence',
    'contribute.target.label.en': 'English Translation',
    'contribute.target.label.ht': 'Haitian Creole Translation',
    'contribute.target.placeholder.en': 'Enter the translation in English...',
    'contribute.target.placeholder.ht': 'Enter the translation in Kreyòl...',
    'contribute.target.hint': 'Your translation of the text above',
    'contribute.context.label': 'Additional Context',
    'contribute.context.optional': '(optional)',
    'contribute.context.placeholder': 'Any additional context or notes about this translation...',
    'contribute.context.hint': 'Example: When to use this phrase, regional variations, etc.',
    'contribute.submit.btn': 'Submit Contribution',
    'contribute.submit.loading': 'Sending...',
    'contribute.success.title': 'Thank You for Your Contribution!',
    'contribute.success.text': "Your translation has been submitted for review. We'll add it to our dataset after verification.",
    'contribute.success.another': 'Add Another Translation',
    'contribute.error': '⚠️ There was an error submitting your contribution. Please try again.',
    'contribute.why.title': 'Why Your Contribution Matters',
    'contribute.benefit1.title': 'Build Better Tools',
    'contribute.benefit1.text': 'Your translations help create more accurate language resources for the Haitian Creole community.',
    'contribute.benefit2.title': 'Preserve Language',
    'contribute.benefit2.text': 'Document authentic Creole phrases and expressions for future generations.',
    'contribute.benefit3.title': 'Help Your Community',
    'contribute.benefit3.text': 'Make healthcare, education, and essential services more accessible in Creole.',
    'contribute.guidelines.title': 'Contribution Guidelines',
    'contribute.guideline1': '✅ Contribute authentic, natural translations you would actually use',
    'contribute.guideline2': '✅ Include common phrases from daily life, work, or specific domains',
    'contribute.guideline3': '✅ Write in standard Haitian Creole orthography when possible',
    'contribute.guideline4': '✅ Add context if the phrase has specific uses or regional variations',
    'contribute.guideline5': "❌ Don't submit machine-translated text",
    'contribute.guideline6': "❌ Don't include offensive or inappropriate content",
  },
  
  ht: {
    // Navigation & Common
    'nav.home': 'Akèy',
    'nav.demo': 'Eseye Demo',
    'nav.contribute': 'Kontribye',
    'nav.docs': 'Dokimantasyon API',
    'nav.back': '← Tounen nan Akèy',
    
    // Landing Page (index.html)
    'index.title': 'Vokal Kreyòl',
    'index.subtitle': 'Enfrastrikti piblik, san objektif likratif, pou aksè nan lang Kreyòl Ayisyen',
    'index.tagline': 'Bati pou kominote yo, edikasyon, jounalis, sante, legal, teknoloji ak sèvis piblik yo.',
    'index.why.title': 'Poukisa Vokal Kreyòl?',
    'index.why.text1': 'Plis pase 12 milyon moun pale Kreyòl Ayisyen, men li toujou pa gen yon bon reprezantasyon nan kesyon bon enfrastrikti lengwistik.',
    'index.why.text2': 'Vokal Kreyòl egziste pou bay sèvis tradiksyon ki egzak, transparan, ak ki baze sou kominote a kòm yon byen piblik — pa yon pwodui komèsyal.',
    'index.what.title': 'Sa Nou Ofri',
    'index.what.item1': '📘 API tradiksyon Kreyòl Ayisyen ↔ Anglè',
    'index.what.item2': '🧠 Tradiksyon ki rezo neronal ibrid  ak yon ansanm done byen etabli',
    'index.what.item3': '🌍 Aksè louvri pou itilizasyon enterè piblik',
    'index.what.item4': '🔎 Fokis sou presizyon ak konsistans lengwistik',
    'index.api.title': 'Itilizasyon API',
    'index.api.note': 'Pa gen otantifikasyon obligatwa pandan faz pilot piblik la.',
    'index.who.title': 'Pou Ki Moun Sa Ye?',
    'index.who.item1': 'Òganizasyon san objektif likratif',
    'index.who.item2': 'Lekòl ak edikatè',
    'index.who.item3': 'Jounalis ak platfòm difisyon',
    'index.who.item4': 'Devlopè k ap konstwi zouti aksesib nan Kreyòl',
    'index.who.item5': 'Enstitisyon piblik',
    'index.ethics.title': 'Gouvènans ak Etik',
    'index.ethics.text': 'Vokal Kreyòl se yon pwojè enfrastrikti piblik san objektif likratif. Nou pa vann done itilizatè yo, epi objektif nou se jesyon kominote  alontèm teknoloji lang Kreyòl Ayisyen.',
    'index.footer.rights': '© 2026 Vokal Kreyòl — Enfrastrikti Lengwistik Piblik',
    'index.footer.contact': 'Kontakte nou:',
    
    // Demo Page (demo.html)
    'demo.title': 'Eseye Vokal Kreyòl',
    'demo.subtitle': 'Fè eksperyans tradiksyon Kreyòl Ayisyen ki egzak',
    'demo.heading': 'Tradiksyon Demo',
    'demo.direction.label': 'Direksyon Tradiksyon:',
    'demo.direction.en-ht': 'Anglè → Kreyòl',
    'demo.direction.ht-en': 'Kreyòl → Anglè',
    'demo.domain.label': 'Domèn:',
    'demo.domain.general': 'Jeneral',
    'demo.domain.healthcare': 'Sante',
    'demo.domain.education': 'Edikasyon',
    'demo.source.en': 'Tèks Anglè',
    'demo.source.ht': 'Tèks Kreyòl Ayisyen',
    'demo.target.en': 'Tradiksyon Anglè',
    'demo.target.ht': 'Tradiksyon Kreyòl Ayisyen',
    'demo.placeholder.en': 'Ekri oswa kole tèks ou a isit la...',
    'demo.placeholder.ht': 'Ekri oswa kole tèks ou a isit la...',
    'demo.chars': 'karaktè',
    'demo.translate.btn': 'Tradui',
    'demo.translate.loading': 'N ap tradui...',
    'demo.confidence.high': 'Konfyans wo',
    'demo.confidence.medium': 'Konfyans mwayen',
    'demo.confidence.low': 'Konfyans ba',
    'demo.warnings.title': '⚠️ Nòt sou Tradiksyon:',
    'demo.feedback.question': 'Èske tradiksyon sa a te itil?',
    'demo.feedback.yes': '👍 Wi, li itil',
    'demo.feedback.no': '👎 Li bezwen amelyorasyon',
    'demo.feedback.placeholder': 'Opsyonèl: Di nou kijan nou ka amelyore tradiksyon sa a...',
    'demo.feedback.submit': 'Voye Kòmantè',
    'demo.feedback.thanks': '✅ Mèsi pou kòmantè ou! Li ede nou amelyore Vokal Kreyòl.',
    'demo.examples.title': 'Eseye egzanp sa yo:',
    'demo.api.title': 'Itilize Vokal Kreyòl nan Aplikasyon Ou',
    'demo.api.text': 'Demo sa a itilize menm API ke ou ka entegre nan aplikasyon ou yo:',
    'demo.api.link': 'Gade Dokimantasyon API Konplè →',
    
    // Contribute Page (contribute.html)
    'contribute.title': 'Kontribye Tradiksyon',
    'contribute.subtitle': 'Ede nou konstwi pi bon zouti pou lang Kreyòl Ayisyen',
    'contribute.description': 'Kontribisyon ou yo ede amelyore kalite tradiksyon pou tout moun. Pataje fraz, mo, oswa tèm ou itilize nan lavi chak jou.',
    'contribute.heading': 'Ajoute yon Nouvo Tradiksyon',
    'contribute.instructions': 'Pataje yon fraz oswa mo ak tradiksyon li. Kontribisyon ou ap revize epi ajoute nan baz done nou.',
    'contribute.name.label': 'Non Ou',
    'contribute.name.optional': '(pou referans)',
    'contribute.name.placeholder': 'Antre non ou (opsyonèl)',
    'contribute.direction.label': 'M ap kontribye nan:',
    'contribute.category.label': 'Kategori:',
    'contribute.source.label.en': 'Tèks Anglè',
    'contribute.source.label.ht': 'Tèks Kreyòl Ayisyen',
    'contribute.source.required': '*',
    'contribute.source.placeholder.en': 'Antre tèks la an Anglè...',
    'contribute.source.placeholder.ht': 'Ekri tèks la an Kreyòl...',
    'contribute.source.hint': 'Antre yon mo, fraz',
    'contribute.target.label.en': 'Tradiksyon Anglè',
    'contribute.target.label.ht': 'Tradiksyon Kreyòl Ayisyen',
    'contribute.target.placeholder.en': 'Antre tradiksyon an Anglè...',
    'contribute.target.placeholder.ht': 'Antre tradiksyon an Kreyòl...',
    'contribute.target.hint': 'Tradiksyon ou a nan tèks ki anlè a',
    'contribute.context.label': 'Kontèks Adisyonèl',
    'contribute.context.optional': '(opsyonèl)',
    'contribute.context.placeholder': 'Nenpòt kontèks oswa nòt adisyonèl sou tradiksyon sa a...',
    'contribute.context.hint': 'Egzanp: Kilè pou itilize fraz sa a, varyasyon rejyonal, elatriye.',
    'contribute.submit.btn': 'Voye Kontribisyon',
    'contribute.submit.loading': 'N ap voye...',
    'contribute.success.title': 'Mèsi pou Kontribisyon Ou!',
    'contribute.success.text': 'Tradiksyon ou te soumèt pou revizyon. Nou pral ajoute li nan baz done nou apre verifikasyon.',
    'contribute.success.another': 'Ajoute yon Lòt Tradiksyon',
    'contribute.error': '⚠️ Te gen yon erè lè w ap soumèt kontribisyon ou. Tanpri eseye ankò.',
    'contribute.why.title': 'Poukisa Kontribisyon Ou Enpòtan',
    'contribute.benefit1.title': 'Konstwi Pi Bon Zouti',
    'contribute.benefit1.text': 'Tradiksyon ou yo ede kreye resous lengwistik ki pi egzak pou kominote Kreyòl Ayisyen an.',
    'contribute.benefit2.title': 'Prezève Lang',
    'contribute.benefit2.text': 'Dokimante fraz ak ekspresyon Kreyòl otantik pou jenerasyon k ap vini yo.',
    'contribute.benefit3.title': 'Ede Kominote Ou',
    'contribute.benefit3.text': 'Fè sèvis sante, edikasyon, ak sèvis esansyèl yo pi aksesib an Kreyòl.',
    'contribute.guidelines.title': 'Règleman pou Kontribisyon',
    'contribute.guideline1': '✅ Kontribye tradiksyon otantik, natirèl ke ou ta reyèlman itilize',
    'contribute.guideline2': '✅ Enkli fraz komen nan lavi chak jou, travay, oswa domèn espesifik',
    'contribute.guideline3': '✅ Ekri nan òtograf Kreyòl Ayisyen estanda lè posib',
    'contribute.guideline4': '✅ Ajoute kontèks si fraz la gen itilizasyon espesifik oswa varyasyon rejyonal',
    'contribute.guideline5': '❌ Pa soumèt tèks ki tradui pa machin',
    'contribute.guideline6': '❌ Pa enkli kontni ofansif oswa enpwopriye',
  }
};

// Current language
let currentLang = 'ht'; // Default to Kreyol

// Initialize language switcher on page load
document.addEventListener('DOMContentLoaded', () => {
  initLanguageSwitcher();
  loadSavedLanguage();
  translatePage();
});

// Initialize language switcher UI
function initLanguageSwitcher() {
  // Create language switcher HTML
  const switcherHTML = `
    <div class="language-switcher">
      <button class="lang-btn" data-lang="ht" title="Kreyòl Ayisyen">
        <span class="lang-flag">🇭🇹</span>
        <span class="lang-text">Kreyòl</span>
      </button>
      <button class="lang-btn" data-lang="en" title="English">
        <span class="lang-flag">🇺🇸</span>
        <span class="lang-text">English</span>
      </button>
    </div>
  `;
  
  // Find header and add language switcher
  const header = document.querySelector('header');
  if (header) {
    const container = header.querySelector('.container') || header;
    const switcherDiv = document.createElement('div');
    switcherDiv.innerHTML = switcherHTML;
    container.insertBefore(switcherDiv.firstElementChild, container.firstChild);
  }
  
  // Add event listeners to language buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      switchLanguage(lang);
    });
  });
  
  // Update active state
  updateActiveLanguage();
}

// Load saved language preference
function loadSavedLanguage() {
  const savedLang = localStorage.getItem('kreyolapi-lang');
  if (savedLang) {
    currentLang = savedLang;
  }
}

// Switch language
function switchLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('kreyolapi-lang', lang);
  updateActiveLanguage();
  translatePage();
}

// Update active language button
function updateActiveLanguage() {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    if (btn.dataset.lang === currentLang) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

// Translate entire page
function translatePage() {
  // Translate all elements with data-i18n attribute
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    const translation = translations[currentLang][key];
    
    if (translation) {
      // Check if element has data-i18n-attr for attribute translation
      const attr = element.getAttribute('data-i18n-attr');
      if (attr) {
        element.setAttribute(attr, translation);
      } else {
        element.textContent = translation;
      }
    }
  });
  
  // Update HTML lang attribute
  document.documentElement.lang = currentLang;
}

// Get translation for a key
function t(key) {
  return translations[currentLang][key] || key;
}

// Export for use in other scripts
window.KreyolAPI = {
  currentLang: () => currentLang,
  t: t,
  switchLanguage: switchLanguage
};

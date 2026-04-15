(function () {
  'use strict';

  var STORAGE_KEY = 'convolving_cookie_consent';
  var GA_ID = 'G-KXNVJ3D6MT';

  function loadGA4() {
    if (window.__ga4Loaded) return;
    window.__ga4Loaded = true;

    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID);
  }

  function buildBanner() {
    var banner = document.createElement('div');
    banner.className = 'cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-live', 'polite');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.innerHTML =
      '<div class="cookie-banner-inner">' +
        '<p class="cookie-banner-text">' +
          'We use cookies to understand how visitors use our site. ' +
          'See our <a href="privacy.html">Privacy Policy</a> for details.' +
        '</p>' +
        '<div class="cookie-banner-actions">' +
          '<button type="button" class="btn btn-outline cookie-btn-reject">Reject</button>' +
          '<button type="button" class="btn cookie-btn-accept">Accept</button>' +
        '</div>' +
      '</div>';
    return banner;
  }

  function showBanner() {
    if (document.querySelector('.cookie-banner')) return;
    var banner = buildBanner();
    document.body.appendChild(banner);

    banner.querySelector('.cookie-btn-accept').addEventListener('click', function () {
      localStorage.setItem(STORAGE_KEY, 'accepted');
      banner.remove();
      loadGA4();
    });
    banner.querySelector('.cookie-btn-reject').addEventListener('click', function () {
      localStorage.setItem(STORAGE_KEY, 'rejected');
      banner.remove();
    });
  }

  function init() {
    var choice = null;
    try { choice = localStorage.getItem(STORAGE_KEY); } catch (e) {}

    if (choice === 'accepted') {
      loadGA4();
    } else if (choice !== 'rejected') {
      showBanner();
    }

    document.addEventListener('click', function (e) {
      var target = e.target.closest && e.target.closest('[data-cookie-prefs]');
      if (!target) return;
      e.preventDefault();
      try { localStorage.removeItem(STORAGE_KEY); } catch (err) {}
      var existing = document.querySelector('.cookie-banner');
      if (existing) existing.remove();
      showBanner();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

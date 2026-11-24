/* Click-to-load YouTube players and the English / Spanish switch on the Task Tutorials page.
   Every <div class="b2ai-video" data-yt="ID" data-lang="en|es" data-title="…"> on the site shows the
   video's thumbnail with a play button; the YouTube player (privacy-enhanced youtube-nocookie.com)
   loads only when it is pressed. */
(function () {
  'use strict';

  var PLAY_ICON = '<svg class="b2ai-video__icon" viewBox="0 0 68 48" aria-hidden="true" focusable="false">' +
    '<path d="M66.5 7.7a8.5 8.5 0 0 0-6-6C55.2.3 34 .3 34 .3s-21.2 0-26.5 1.4a8.5 8.5 0 0 0-6 6C.1 13 .1 24 .1 24s0 11 1.4 16.3a8.5 8.5 0 0 0 6 6C12.8 47.7 34 47.7 34 47.7s21.2 0 26.5-1.4a8.5 8.5 0 0 0 6-6C67.9 35 67.9 24 67.9 24s0-11-1.4-16.3z"/>' +
    '<path class="b2ai-video__arrow" d="M45 24 27 14v20z"/></svg>';

  function showThumbnail(el) {
    var id = el.getAttribute('data-yt');
    var lang = el.getAttribute('data-lang') === 'es' ? 'es' : 'en';
    var title = el.getAttribute('data-title') || 'Video';
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'b2ai-video__play';
    button.setAttribute('aria-label', 'Play: ' + title);  // interface labels stay in English
    var img = document.createElement('img');
    img.src = 'https://i.ytimg.com/vi/' + encodeURIComponent(id) + '/hqdefault.jpg';
    img.alt = '';
    img.loading = 'lazy';
    img.decoding = 'async';
    button.appendChild(img);
    button.insertAdjacentHTML('beforeend', PLAY_ICON);
    button.addEventListener('click', function () { play(el); });
    el.classList.remove('b2ai-video--playing');
    el.innerHTML = '';
    el.appendChild(button);
  }

  function play(el) {
    var id = el.getAttribute('data-yt');
    var lang = el.getAttribute('data-lang') === 'es' ? 'es' : 'en';
    var frame = document.createElement('iframe');
    frame.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) +
      '?autoplay=1&rel=0&hl=' + lang + '&cc_lang_pref=' + lang;
    frame.title = el.getAttribute('data-title') || 'YouTube video';
    frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    el.innerHTML = '';
    el.appendChild(frame);
    el.classList.add('b2ai-video--playing');
    frame.focus();
  }

  var videos = document.querySelectorAll('.b2ai-video[data-yt]');
  for (var i = 0; i < videos.length; i++) showThumbnail(videos[i]);

  // Language switch (Task Tutorials page only)
  var root = document.getElementById('b2ai-tut');
  if (!root) return;
  var KEY = 'b2ai-tutorial-lang';

  function setLang(lang, remember) {
    root.setAttribute('data-lang', lang);
    var buttons = root.querySelectorAll('[data-set-lang]');
    for (var j = 0; j < buttons.length; j++) {
      var on = buttons[j].getAttribute('data-set-lang') === lang;
      buttons[j].classList.toggle('bx-chip--on', on);
      buttons[j].setAttribute('aria-pressed', String(on));
    }
    // Stop any playing video: switching language hides it
    var playing = root.querySelectorAll('.b2ai-video--playing');
    for (var k = 0; k < playing.length; k++) showThumbnail(playing[k]);
    if (remember) {
      try { localStorage.setItem(KEY, lang); } catch (e) { /* storage unavailable */ }
    }
  }

  root.addEventListener('click', function (e) {
    var b = e.target.closest('[data-set-lang]');
    if (b) setLang(b.getAttribute('data-set-lang'), true);
  });

  var fromUrl = new URLSearchParams(location.search).get('lang');
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) { /* storage unavailable */ }
  setLang(fromUrl === 'es' || fromUrl === 'en' ? fromUrl : (saved === 'es' ? 'es' : 'en'), false);
})();

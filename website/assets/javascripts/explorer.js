/* Variable Explorer: search every current and past REDCap variable and show its history.
   Data: assets/data/variables.json (scripts/build_data_dictionary_docs.py --json). */
(function () {
  'use strict';
  var root = document.getElementById('bx');
  if (!root) return;

  var input = document.getElementById('bx-q');
  var filtersEl = document.getElementById('bx-filters');
  var listEl = document.getElementById('bx-list');
  var countEl = document.getElementById('bx-count');
  var detailEl = document.getElementById('bx-detail');
  var base = (root.getAttribute('data-base') || '.').replace(/\/$/, '');
  var repo = root.getAttribute('data-repo') || '';
  var PAGE = 60;

  var FILTERS = [
    ['all', 'All'], ['active', 'Active'], ['renamed', 'Renamed'],
    ['retired', 'Retired'], ['previous', 'Previous version'], ['removed', 'Removed']
  ];
  var STATUS_TEXT = { active: 'Active', retired: 'Retired · still in REDCap', previous: 'Previous version · still in REDCap', removed: 'Removed' };
  var state = { q: '', filter: 'all', limit: PAGE, selected: null };
  var vars = [];
  var byName = {};

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function pageUrl(v) {
    var path = v.p.replace(/\.md$/, '/');
    return base + '/' + path.split('/').map(encodeURIComponent).join('/') + (v.a ? '#' + encodeURIComponent(v.a) : '');
  }
  function releaseLink(tag) {
    return '<a href="' + esc(repo) + '/releases/tag/' + encodeURIComponent(tag) + '">' + esc(tag) + '</a>';
  }
  function statusOf(v) { return v.s; }
  function passes(v, f) {
    if (f === 'all') return true;
    if (f === 'renamed') return v.fo.length > 0;
    return statusOf(v) === f;
  }

  function matches() {
    var q = state.q.trim().toLowerCase();
    var out = [];
    for (var i = 0; i < vars.length; i++) {
      var v = vars[i];
      if (!passes(v, state.filter)) continue;
      if (!q) { out.push([2, v]); continue; }
      var name = v.n.toLowerCase();
      var rank = -1;
      if (name === q || v.fo.indexOf(q) !== -1) rank = 0;
      else if (name.indexOf(q) === 0) rank = 1;
      else if (name.indexOf(q) !== -1 || v.fo.some(function (o) { return o.indexOf(q) !== -1; })) rank = 2;
      else if (v.l.toLowerCase().indexOf(q) !== -1 || v.i.toLowerCase().indexOf(q) !== -1) rank = 3;
      if (rank >= 0) out.push([rank, v]);
    }
    out.sort(function (a, b) { return a[0] - b[0]; });
    return out.map(function (x) { return x[1]; });
  }

  function renderFilters() {
    filtersEl.innerHTML = FILTERS.map(function (f) {
      var n = vars.filter(function (v) { return passes(v, f[0]); }).length;
      var on = state.filter === f[0];
      return '<button type="button" class="bx-chip' + (on ? ' bx-chip--on' : '') + '" aria-pressed="' + on + '" data-filter="' + f[0] + '">' +
        esc(f[1]) + ' <span>' + n.toLocaleString() + '</span></button>';
    }).join('');
  }

  function renderList() {
    var found = matches();
    countEl.textContent = found.length === 1 ? '1 variable' : found.length.toLocaleString() + ' variables';
    if (!found.length) {
      listEl.innerHTML = '<p class="bx-none">No variable matches that search with this filter. Try part of the name, or choose All.</p>';
      return;
    }
    var html = found.slice(0, state.limit).map(function (v) {
      var sel = state.selected === v.n;
      var former = v.fo.length ? ' · formerly ' + esc(v.fo.join(', ')) : '';
      return '<button type="button" class="bx-item' + (sel ? ' bx-item--on' : '') + '" data-name="' + esc(v.n) + '"' + (sel ? ' aria-current="true"' : '') + '>' +
        '<code>' + esc(v.n) + '</code>' +
        '<span class="bx-item__label">' + esc(v.l || '(no label)') + '</span>' +
        '<span class="bx-item__meta"><i class="bx-dot bx-dot--' + statusOf(v) + '" aria-hidden="true"></i>' + esc(v.i) + former + '</span>' +
        '</button>';
    }).join('');
    if (found.length > state.limit) {
      html += '<button type="button" class="b2ai-btn bx-more" data-more="1">Show ' +
        Math.min(PAGE, found.length - state.limit) + ' more of ' + (found.length - state.limit).toLocaleString() + '</button>';
    }
    listEl.innerHTML = html;
  }

  function renderDetail() {
    var v = byName[state.selected];
    if (!v) {
      detailEl.innerHTML = '<p class="bx-empty">Choose a variable to see its history.</p>';
      return;
    }
    var events = v.e.map(function (e) {
      return '<li><span class="bx-tl__dot" aria-hidden="true"></span><div>' +
        '<span class="bx-tl__head">' + releaseLink(e[0]) + ' · ' + esc(e[1]) + ' · ' + esc(e[2]) + '</span>' +
        '<span class="bx-tl__text">' + esc(e[3]) + '</span></div></li>';
    }).join('');
    detailEl.innerHTML =
      '<span class="bx-crumbs">' + esc(v.c) + ' › ' + esc(v.i) + '</span>' +
      '<h2><code>' + esc(v.n) + '</code></h2>' +
      '<p class="bx-label">' + esc(v.l || '(no label)') + '</p>' +
      '<span class="bx-status bx-status--' + statusOf(v) + '">' + esc(STATUS_TEXT[statusOf(v)] || statusOf(v)) +
      (v.fo.length ? ' · formerly ' + esc(v.fo.join(', ')) : '') + '</span>' +
      '<dl class="bx-facts">' +
      '<div><dt>Type</dt><dd>' + esc(v.t) + '</dd></div>' +
      '<div><dt>Values</dt><dd>' + esc(v.v || '—') + '</dd></div>' +
      '<div><dt>Introduced</dt><dd>' + releaseLink(v.in) + '</dd></div>' +
      '</dl>' +
      '<h3>History</h3><ol class="bx-tl">' + events + '</ol>' +
      '<a class="b2ai-btn b2ai-btn--primary" href="' + esc(pageUrl(v)) + '">Open in the data dictionary</a>';
  }

  function select(name, push) {
    if (!byName[name]) return;
    name = byName[name].n; // a former name selects the variable it became
    state.selected = name;
    renderList();
    renderDetail();
    if (push !== false) history.replaceState(null, '', '#' + encodeURIComponent(name));
    if (window.matchMedia('(max-width: 76.1875em)').matches) detailEl.scrollIntoView({ block: 'start' });
  }

  filtersEl.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-filter]');
    if (!b) return;
    state.filter = b.getAttribute('data-filter');
    state.limit = PAGE;
    renderFilters();
    renderList();
  });
  listEl.addEventListener('click', function (e) {
    var more = e.target.closest('[data-more]');
    if (more) { state.limit += PAGE; renderList(); return; }
    var b = e.target.closest('button[data-name]');
    if (b) select(b.getAttribute('data-name'));
  });
  input.addEventListener('input', function () {
    state.q = input.value;
    state.limit = PAGE;
    renderList();
  });

  fetch(root.getAttribute('data-src'))
    .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
    .then(function (data) {
      vars = data.variables;
      vars.forEach(function (v) { byName[v.n] = v; v.fo.forEach(function (o) { if (!byName[o]) byName[o] = v; }); });
      renderFilters();
      var fromHash = decodeURIComponent(location.hash.slice(1));
      var start = byName[fromHash] ? byName[fromHash].n : null;
      if (start) { state.q = start; input.value = start; }
      renderList();
      if (start) select(start, false); else renderDetail();
    })
    .catch(function (err) {
      countEl.textContent = 'The variable list could not be loaded (' + err.message + '). Reload the page to try again.';
    });
})();

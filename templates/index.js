/* Breakage index: sort by # or severity, filter by severity. Only touches the index table;
   without JavaScript the table stays in ID order with every row shown. */
(function () {
  var sec = document.getElementById("index");
  if (!sec) return;
  var tools = sec.querySelector(".idx-tools"), tbody = sec.querySelector("tbody");
  var rows = [].slice.call(tbody.rows), chips = [].slice.call(tools.querySelectorAll(".chip"));
  var count = tools.querySelector(".idx-count"), heads = sec.querySelectorAll("thead th");
  var state = { key: "n", dir: 1, sevs: {} };  // dir 1: N1 first, or Critical first

  var sorts = [[heads[0], "n", "Sort by number"], [heads[1], "rank", "Sort by severity"]].map(function (s) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "sort";
    b.title = s[2];
    b.innerHTML = s[0].innerHTML + '<span class="arr" aria-hidden="true"></span>';
    s[0].textContent = "";
    s[0].appendChild(b);
    b.addEventListener("click", function () {
      state.dir = state.key === s[1] ? -state.dir : 1;
      state.key = s[1];
      apply();
    });
    return { th: s[0], key: s[1], arr: b.lastChild };
  });

  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var s = c.dataset.sev;
      if (!s) state.sevs = {};
      else if (state.sevs[s]) delete state.sevs[s];
      else state.sevs[s] = true;
      apply();
    });
  });

  function apply() {
    var k = state.key, any = Object.keys(state.sevs).length > 0, shown = 0;
    rows.sort(function (a, b) {
      return (a.dataset[k] - b.dataset[k]) * state.dir || a.dataset.n - b.dataset.n;
    });
    rows.forEach(function (r) {
      r.hidden = any && !state.sevs[r.dataset.sev];
      if (!r.hidden) shown++;
      tbody.appendChild(r);
    });
    chips.forEach(function (c) {
      c.setAttribute("aria-pressed", c.dataset.sev ? !!state.sevs[c.dataset.sev] : !any);
    });
    sorts.forEach(function (s) {
      var on = s.key === k;
      if (on) s.th.setAttribute("aria-sort", state.dir === 1 ? (k === "n" ? "ascending" : "descending") : (k === "n" ? "descending" : "ascending"));
      else s.th.removeAttribute("aria-sort");
      s.arr.textContent = !on ? "↕" : (k === "n") === (state.dir === 1) ? "↑" : "↓";
    });
    count.textContent = any ? "Showing " + shown + " of " + rows.length : rows.length + " breakages";
  }

  tools.hidden = false;
  apply();
})();

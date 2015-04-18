// Highlight navbar-brand when at root
var is_root = location.pathname == "/";
if (is_root) {
    $("a.navbar-brand").addClass("active");
};

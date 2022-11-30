// Builds on http://chris-said.io/2016/02/13/how-to-make-polished-jupyter-presentations-with-optional-code-visibility/
// to inject a navbar button in the nbviewer UI and to make the snippet easily reusable across notebooks, i.e.:
// %%html
// <script src="https://cdn.rawgit.com/parente/4c3e6936d0d7a46fd071/raw/b8adbd09bceb590c35c3cdf541a2cd0e799ec85e/code_toggle.js"></script>
$(document).ready(function(){
    window.code_toggle = function() {
        (window.code_shown) ? $('div.input').hide(250) : $('div.input').show(250);
        window.code_shown = !window.code_shown
    }
    if($('body.nbviewer').length) {
        $('<li><a href="javascript:window.code_toggle()" title="Show/Hide Code"><span class="fa fa-code fa-2x menu-icon"></span><span class="menu-text">Show/Hide Code</span></a></li>').appendTo('.navbar-right');
        window.code_shown=false;
        $('div.input').hide();
    }
});

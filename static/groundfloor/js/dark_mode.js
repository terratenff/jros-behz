/**
 * @file
 * Provides the functions to switch between light and dark mode,
 * and remembers user choice via cookies.
 */

/**
 * Enables, or disables, "dark mode" of the web page. Uses a cookie
 * to remember user's choice.
 */
function toggleDarkMode() {
    var option = readCookie("darkmode");
    var optionReverse = "true";
    var stylesheet = document.getElementById("sitestyle");

    var styleName = "/static/groundfloor/css/dark";
    if (option === "true") {
        optionReverse = "false";
        styleName = "/static/groundfloor/css/light";
    }

    stylesheet.href = styleName + ".css";
    createCookie("darkmode", optionReverse);
    console.log("OPTION (SAVE): " + optionReverse);
}

/**
 * Initialization function for the web page, in terms of either
 * enabling or disabling "dark mode".
 */
function initialize() {
    var option = readCookie("darkmode");
    console.log("OPTION (LOAD): " + option);

    var head = document.head;
    var link = document.createElement("link");
    link.type = "text/css";
    link.rel = "stylesheet";
    link.id = "sitestyle";

    var styleName = "/static/groundfloor/css/light";
    if (option === "true") {
        console.log("OPTION (LOAD - PASS): " + option);
        styleName = "/static/groundfloor/css/dark";
    }
    console.log("STYLE: " + styleName);
    link.href = styleName + ".css";
    head.appendChild(link);
}

initialize();

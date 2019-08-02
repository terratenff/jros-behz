/**
 * @file
 * Performs simple cookie management for the web application.
 */

/**
 * Creates a cookie, based on provided parameters.
 * @param name Name of the cookie
 * @param value The value of the cookie
 * @param days The duration of the cookie in terms of days
 */
function createCookie(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = "; expires" + date.toGMTString();
    }
    else var expires = "";

    document.cookie = name + "=" + value + expires + "; path=/";
}

/**
 * Reads a cookie specified in the provided parameter.
 * @param name Name of the cookie
 * @return The value of the cookie
 */
function readCookie(name) {
    var cookieName = name + "=";
    var contents = document.cookie.split(";");
    for (var i = 0; i < contents.length; i++) {
        var c = contents[i];

        while (c.charAt(0) == ' ') {
            c = c.substring(1, c.length);
        }

        if (c.indexOf(cookieName) == 0) {
            return c.substring(cookieName.length, c.length);
        }
    }
    return null;
}

/**
 * Deletes a cookie, specified by the provided parameter.
 * @param name Name of the cookie
 */
function eraseCookie(name) {
    createCookie(name, "", -1);
}

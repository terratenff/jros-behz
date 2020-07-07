/**
 * @file
 * Creates a "privacy policy" notice for the user. If the user
 * has already dismissed it, it won't be created again (this
 * is remembered via cookies).
 */

/**
 * Creates a privacy notice that sticks to the bottom of
 * the browser, for the user to see. If the user has already
 * dismissed it, the privacy notice won't be created again.
 */
function createPrivacyNotice() {
    var option = readCookie("privacynotice");
    console.log("Privacy Notice: " + option);
    if (option === null) {
        var element = document.createElement("div");
        element.setAttribute("id", "privacy_notice");
        var paragraph = document.createElement("p");
        var text = document.createTextNode("By using this website, you agree to be aware that this site stores a cookie for toggling dark mode. ");
        paragraph.appendChild(text);

        var button = document.createElement("button");
        var buttonText = document.createTextNode("Dismiss");
        button.appendChild(buttonText);
        button.addEventListener("click", dismissPrivacyNotice);

        element.appendChild(paragraph);
        element.appendChild(button);
        document.getElementsByTagName("body")[0].appendChild(element);
    }
}

/**
 * Dismisses the privacy notice, and creates a cookie,
 * so as to ensure it won't show itself to the user again.
 */
function dismissPrivacyNotice() {
    var element = document.getElementById("privacy_notice");
    element.parentNode.removeChild(element);
    createCookie("privacynotice", "false");
}

createPrivacyNotice();

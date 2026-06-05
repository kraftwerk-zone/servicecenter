document.addEventListener("DOMContentLoaded", function () {
  var header = document.querySelector("header.md-header, .md-header");
  if (!header) {
    return;
  }

  var target = header.querySelector(".md-header__inner") || header;

  var langs = {
    de: "Deutsch",
    en: "English",
    es: "Español",
    it: "Italiano",
    cs: "Čeština",
    da: "Dansk",
  };

  var path = window.location.pathname.replace(/^\/+|\/+$/g, "");
  var parts = path.split("/");
  var locale = "de";
  if (parts[0] === "docs") {
    locale = langs[parts[1]] ? parts[1] : "de";
  } else {
    locale = langs[parts[0]] ? parts[0] : "de";
  }

  var languageLabel = document.createElement("span");
  languageLabel.className = "kg-language-indicator";
  languageLabel.textContent = langs[locale] || locale.toUpperCase();

  var button = document.createElement("a");
  button.className = "kg-shop-back-button";
  button.href = "https://kraftwerk.shop";
  button.textContent = "Zurück zum Shop";
  button.setAttribute("aria-label", "Zurück zum Shop");

  var searchToggle = target.querySelector('label[for="__search"]');
  var selectBlock = target.querySelector('.md-header__option');

  if (selectBlock && searchToggle) {
    selectBlock.parentNode.insertBefore(languageLabel, searchToggle);
  } else {
    target.insertBefore(languageLabel, target.firstChild);
  }

  var logo = target.querySelector('.md-logo');
  if (logo && logo.nextSibling) {
    target.insertBefore(button, logo.nextSibling);
  } else {
    target.insertBefore(button, target.firstChild);
  }
});

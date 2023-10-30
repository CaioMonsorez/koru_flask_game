// teste

// =============================================================================================================
// BootsTrap - Sistema de Grid Padrão

// Abre e fecha menu lateral em modo mobile

const menuMobile = document.querySelector('.menu-mobile')
const body = document.querySelector('body')
// body-class="body_pagIndex

menuMobile.addEventListener('click', () => {
    menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x", "bi-list");
    body.classList.toggle("menu-nav-active");
});

// =============================================================================================================

// Fechar o menu quando clicar em algum item/link da barra lateral e muda o ícone Hamburguer para List (pois antes está em X)

// Vamos usar a class nav-item do asaid:

// Vamos pegar o nav.item:
const navItem = document.querySelectorAll('.nav-item')
// Podemos verificar pedindo um console.log no inspencionar
// console.log(navItem)
// ele traz um array de todos nav-item
navItem.forEach(item => {
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")) {
            body.classList.remove("menu-nav-active")
            menuMobile.classList.replace("bi-x", "bi-list");
        }
    })
})

// =============================================================================================================
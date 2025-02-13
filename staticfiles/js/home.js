window.addEventListener('scroll', function () {
    const containers = [
        document.getElementById('nav-hosto'),
        document.getElementById('nav-hosto-prompt'),
        document.getElementById('nav-hosto-interne'),
        document.getElementById('nav-hosto-operation'),
        document.getElementById('nav-hosto-pharma'),
        document.getElementById('footer')
    ]
    const windowHeight = window.innerHeight 
    const scrollPosition = window.scrollY
    containers.forEach(container => {
        const divs = container.querySelectorAll('.item')
        divs.forEach(div => {
            const divTop  = div.getBoundingClientRect().top  + scrollPosition
            const divBottom = divTop + div.offsetHeight 
            const start = scrollPosition
            const end = scrollPosition + windowHeight 
            if (divBottom > start && divTop < end ) {
                div.classList.add('visible')
            }else {
                div.classList.remove('visible')
            }
        })
    })
})
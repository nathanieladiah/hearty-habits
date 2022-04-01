const navItems = document.querySelectorAll('.nav-item')

function setActive(e) {
	const parent = e.target.parentNode
	const active = parent.querySelector('.active')
	if (active) {
		active.classList.toggle('active')
	}
	e.target.classList.add('active')
}

navItems.forEach(listItem => {
	listItem.addEventListener('click', setActive)
})
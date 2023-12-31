function getCookie(name) {
	let cookieValue = null
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';')
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim()
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + '=') {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
				break
			}
		}
	}
	return cookieValue
}

const addToCart = id => {
	$.ajax({
		type: 'POST',
		url: '/cart/add/',
		data: {
			productId: id,
			quantity: $('#select option:selected').text(),
			action: 'post',
		},
		headers: {
			'X-Requested-With': 'XMLHttpRequest',
			'X-CSRFToken': getCookie('csrftoken'),
		},
		success: res => {
			document.getElementById('cart-quantity').textContent = res.quantity
			document.getElementById('cart-quantity-mobile').textContent = res.quantity
		},
		error: err => {
			console.log(err)
		},
	})
}

const removeItem = id => {
	$.ajax({
		url: '/cart/remove/',
		data: {
			action: 'delete',
			productId: id,
		},
		success: res => {
			document.getElementById(id).innerText = ''
			document.getElementById('cart-quantity').innerText = res.quantity
			document.getElementById('cart-quantity-mobile').innerText = res.quantity
			document.getElementById('total').innerText = `Total price: £${res.total}`
		},
		error: error => {
			console.log(error)
		},
	})
}

const updateCart = id => {
	let selectedValue = $(`#select${id} option:selected`).text()
	$.ajax({
		url: '/cart/update/',
		data: {
			action: 'put',
			productId: id,
			quantity: selectedValue,
		},
		headers: {
			'X-Requested-With': 'XMLHttpRequest',
			'X-CSRFToken': getCookie('csrftoken'),
		},
		success: res => {
			document.getElementById('cart-quantity').innerText = res.quantity
			document.getElementById(`sub-total-${id}`).innerText = res.sub_total
			document.getElementById('total').innerText = `Total price: £${res.total}`
		},
		error: error => {
			console.log(error)
		},
	})
}

const dismissibleAlertList = document.querySelectorAll('.alert-dismissible')
dismissibleAlertList.forEach(function (alert) {
	new bootstrap.Alert(alert)
	setTimeout(() => {
		alert.classList.add('d-none')
	}, 3500)
})

const addToCart = (id) => {
	$.ajax({
		url: '/cart/add/',
		data: {
			productId: id,
			quantity: $('#select option:selected').text(),
			csrfmiddlewaretoken: '{{ csrf_token }}',
			action: 'post',
		},
		success: function (res) {
			document.getElementById('cart-quantity').innerText = res.quantity
		},
		error: function (xhr, errmsg, err) {
			console.log(err)
		},
	})
}

const removeItem = (id) => {
	$.ajax({
		url: '/cart/remove/',
		data: {
			action: 'delete',
			csrfmiddlewaretoken: '{{ csrf_token }}',
			productId: id,
		},
		success: res => {
			document.getElementById(res.id).innerText = ''
			document.getElementById('cart-quantity').innerText = res.quantity
			document.getElementById('total').innerText = `Total price: £${res.total}`
		},
		error: error => {
			console.log(error)
		},
	})
}

const baseEndpoint = 'http://localhost:8000/api'
	// const deleteBtns = document.getElementsByClassName('delete-btn')
	const deleteBtns = document.querySelectorAll('.delete-btn')
	const deleteForm = document.getElementById('deleteTreatForm')
	// let navigate = useNavigate();

	// getElementByClassName does not return an array
	// use Array.from(result).forEach()
	// or 
	// for (const result of results) {}

	deleteBtns.forEach(btn => {
		btn.onclick = () => {
			const product_id = btn.dataset.treat;
			getProduct(product_id)
		}
	})

	// function getProduct(product_id) {
	// 	fetch(`${baseEndpoint}/treat/${product_id}`)
	// 	.then(response => response.json())
	// 	.then(data => {
	// 		// console.log(data);
	// 		return data;
	// 	})
	// }

	// use an async await to wait for the actual values to come back

	let getProduct = async (product_id) => {
		let response = await fetch(`${baseEndpoint}/treat/${product_id}/`)
		let data = await response.json()
		// return data
		// console.log(data.id)


		// deleteForm.dataset.id = data.id

		let action =  `/administrator/treats/delete/${data.id}/`;
		deleteForm.action = action;

		// console.log(deleteForm.action)
	}

// -------------------------------------------

	// async function getProduct(product_id) {
	// 	let response = await fetch(`${baseEndpoint}/treat/${product_id}`);
	// 	let treat = await response.json();

	// 	console.log(treat)
	// }

// -----------------------------------	

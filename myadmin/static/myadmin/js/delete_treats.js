const deleteBtns = document.querySelectorAll('.delete-btn')
const deleteForm = document.getElementById('deleteTreatForm')

deleteBtns.forEach(btn => {
	btn.onclick = () => {
		const treat_id= btn.dataset.treat;
		
		let action = `/admin/treats/delete/${treat_id}/`;
		deleteForm.action = action;
	}
})


const deleteBtns = document.querySelectorAll('.delete-btn')
const deleteForm = document.getElementById('deleteUserForm')

deleteBtns.forEach( btn => {
	btn.onclick = () => {
		const user_id = btn.dataset.user;

		let action = `/admin/users/delete/${user_id}/`;
		deleteForm.action = action;
	}
})
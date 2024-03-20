function confirmDelete() {
    if (confirm('Are you sure you want to delete this project?')) {
        document.getElementById('delete-form').submit();
    }
}

function confirmDelete() {
    if (confirm('Are you sure you want to delete this project?')) {
        document.getElementById('delete-form').submit();
    }
}


const tweentop = KUTE.fromTo(
    '#wave-top-1',
    { path: '#wave-top-1' },
    { path: '#wave-top-2' },
    { repeat: Infinity, duration: 1000, yoyo: true }
).start();

const tweenbottom = KUTE.fromTo(
    '#wave-bottom-1',
    { path: '#wave-bottom-1' },
    { path: '#wave-bottom-2' },
    { repeat: Infinity, duration: 1000, yoyo: true }
).start();
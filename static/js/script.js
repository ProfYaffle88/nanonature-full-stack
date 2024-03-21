function confirmDelete() {
    if (confirm('Are you sure you want to delete this project?')) {
        document.getElementById('delete-form').submit();
    }
}


const tween1 = KUTE.fromTo(
    '#wave-top-1',
    { path: '#wave-top-1' },
    { path: '#wave-top-2' },
    { repeat: Infinity, duration: 700, yoyo: true }
).start();

const tween2 = KUTE.fromTo(
    '#wave-bottom-1',
    { path: '#wave-bottom-1' },
    { path: '#wave-bottom-2' },
    { repeat: Infinity, duration: 700, yoyo: true }
).start();
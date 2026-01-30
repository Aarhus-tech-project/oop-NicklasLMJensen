const deleteButtons = document.querySelectorAll('.delete-btn');
const editable = document.querySelectorAll('.editable')


deleteButtons.forEach(button => {
    button.addEventListener('click', async (e) => {
        const bookId = button.dataset.id;
        deleteBook(bookId);
    });
});

function deleteBook(id) {
    const url = "/books/" + id;
    fetch(url, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            console.log("Book deleted successfully");
            window.location.reload();
        } else {
            console.error("Failed to delete the book");
        }
    });
}



editable.forEach(cell => {
    cell.addEventListener('blur', async (e) => {
        const id = cell.dataset.id;
        const field = cell.dataset.field;
        const newValue = cell.innerText; 

        fetch(`/books/${id}`, {
            method: 'PATCH',
            headers: { 'Conent-Type': 'application/json' },
            body: JSON.stringify({ [field]: newValue })
        })
        .then(response => {
            if (response.ok) {
                console.log("Book updated successfully");
            }
        });
    });
});

Callback.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        e.target.blur();
    }
});
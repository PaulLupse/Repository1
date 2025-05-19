console.log('a')

async function getCatalog()
{
    const url = "http://127.0.0.1:5000";
    const catalogData = await fetch(url.concat("/books"));
    return await catalogData.json();
}
async function getBook(bookId)
{
    const url = "http://127.0.0.1:5000";
    const bookData = await fetch(url.concat(`/books/${bookId}`));
    return await bookData.json();
}
async function clearTable(tableId)
{
    var table = document.getElementById(tableId);
    const tableRowCount = table.rows.length;
    for(let index = 1; index < tableRowCount; index++)
    {
        table.deleteRow(1);
    }
}
async function showBook(tableId) {
    const bookId = document.getElementById("book_id_input").value;
    await clearTable(tableId);
    const bookData = await getBook(bookId);
    const fieldsOrder = bookData[0]['order'];
    const entry = bookData[1];
    addRow(tableId, entry, fieldsOrder);
}
export async function showCatalog(tableId)
{
    await clearTable(tableId);
    const catalogData = await getCatalog();
    const catalogFieldsOrder = catalogData[0]['order'];
    const catalogDataSize = catalogData.length;
    for (let index = 1; index < catalogDataSize; index ++)
    {
        const catalogEntry = catalogData[index];
        addRow(tableId, catalogEntry, catalogFieldsOrder);
    }
}
function addRow(tableId, rowData, catalogFieldsOrder)
{
    var table = document.getElementById(tableId);
    const tableRowCount = table.rows.length;
    var row = table.insertRow(tableRowCount);
    const fieldsCount = Object.keys(catalogFieldsOrder).length;
    for(let index = 0; index < fieldsCount; index ++)
    {
        var cell = row.insertCell(index);
        cell.innerHTML = rowData[catalogFieldsOrder[index]];
    }
}
async function addBook()
{
    let bookTitle = document.getElementById("book_title").value;
    let bookAuthor = document.getElementById("book_author").value;
    let bookReleaseYear = document.getElementById("book_release_date").value;
    let bookStock = document.getElementById("book_stock").value;
    let bookPrice = document.getElementById("book_price").value;

    if(bookTitle === "")
        bookTitle = "-"
    if(bookAuthor === "")
        bookAuthor = "-"
    if(bookReleaseYear === "")
        bookReleaseYear = "-"
    if(bookStock === "")
        bookStock = "-"
    if(bookPrice === "")
        bookPrice = "-"

    const url = "http://127.0.0.1:5000";
    const response = await fetch(url.concat(`/books`),
        {
            method:"POST",
            body: JSON.stringify({title: bookTitle,
                author: bookAuthor, year_published:bookReleaseYear,
                stock: bookStock, price: bookPrice
            }),
            headers:{"Content-type": "application/json; charset=UTF-8"}
            }
        );
    if(response.ok)
    {
        await showCatalog('catalog');
        alert("Added succesfully");
    }
    else
    {
        alert("Error");
    }
}

async function updateBook()
{
    let bookTitle = document.getElementById("book_title").value;
    let bookAuthor = document.getElementById("book_author").value;
    let bookReleaseYear = document.getElementById("book_release_date").value;
    let bookStock = document.getElementById("book_stock").value;
    let bookPrice = document.getElementById("book_price").value;

            let fields = {};
            if(bookTitle !== "")
                fields["title"] = bookTitle;
            if(bookAuthor !== "")
                fields["author"] = bookAuthor;
            if(bookReleaseYear !== "")
                fields["year_published"] = bookReleaseYear;
            if(bookStock !== "")
                fields["stock"] = bookStock;
            if(bookPrice !== "")
                fields["price"] = bookPrice;

            const bookId = document.getElementById("book_id_input").value;
            const url = "http://127.0.0.1:5000";
            const response = await fetch(url.concat(`/books/${bookId}`),
                    {
                        method:"PUT",
                        body: JSON.stringify(fields),
                        headers:{"Content-type": "application/json; charset=UTF-8"}
                    }
            );
            if(response.ok)
            {
                await showCatalog('catalog');
                alert("Updated succesfully");
            }
            else
            {
                alert("Error");
            }
}
async function deleteBook()
{
            const bookId = document.getElementById("book_id_input").value;

            const url = "http://127.0.0.1:5000";
            const response = await fetch(url.concat(`/books/${bookId}`),{method:"DELETE"});

            if(response.ok)
            {
                await showCatalog('catalog');
                alert("Deleted succesfully");
            }
            else
            {
                alert("Error");
            }
}
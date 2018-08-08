const Product = ({id, name, image, cost}) => (
    `<div class="block">
        <a href="../description${id}">
            <img src="/media/${ image }">
            <div class="nameToys">${ name }</div>
            <div class="price">&#8381; ${ cost }</div>
        </a>
    </div>`
)


const renderData = res => {
    prod_html = res.data.results.map(Product).join('')
    container = document.getElementById('product-list')
    container.innerHTML = prod_html
}

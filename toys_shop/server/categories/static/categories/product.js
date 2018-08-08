const Product = ({id, category_id, category_name, name, image, content, cost}) => (
    `<div class="blockHeader">
        <a href="{% url 'categories:group' ${category_id} %}">${ category_name }</a> / ${ name }
    </div>
    <div class="blockId">
        <a href="/media/${ image }" target="_blank">
            <div class="imageId"><img src="/media/${ image }"></div>
        </a>
        <div class="description">
            <h3>Описание</h3>
            <div>${ content }<div>
                <div class="priceId">&#8381; ${ cost } <br><p></p></div>
            <a href="#">купить</a>
        </div>
    </div>
   `
)


const renderData = res => {
    prod_html = res.data.results.map(Product).join('')
    container = document.getElementById('product-list')
    container.innerHTML = prod_html
}

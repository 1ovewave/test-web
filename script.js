// 取得金價並展示
fetch('api/getPrices.php')
    .then(response => response.json())
    .then(data => {
        const table = document.querySelector("#price-list table");
        data.forEach(item => {
            const row = document.createElement("tr");
            row.innerHTML = `<td>${item.gold_type}</td><td>${item.price_per_gram}</td><td>${item.updated_at}</td>`;
            table.appendChild(row);
        });
    });

// 計算功能
function calculate() {
    const weight = document.getElementById('gold-weight').value;
    const price = parseFloat(document.querySelector("#price-list table tr:nth-child(2) td:nth-child(2)").innerText);
    if (weight && price) {
        document.getElementById('result').innerText = `回收金額：${(weight * price).toFixed(2)} 元`;
    }
}

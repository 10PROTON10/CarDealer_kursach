// Получение CSRF-токена из cookies
const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    .split('=')[1];

function addToFavorites(carId) {
    const token = localStorage.getItem('access_token');
    console.log('Token:', token);

    fetch(`/api/add_to_favorites/${carId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data);
    })
    .catch(error => console.error('Error:', error));
}

function searchCars() {
    // Получение значений из формы
    const brand = document.getElementById('brand').value;
    const priceFrom = document.getElementById('price_from').value;
    const priceTo = document.getElementById('price_to').value;
    const yearFrom = document.getElementById('year_from').value;
    const yearTo = document.getElementById('year_to').value;
    const mileage = document.getElementById('mileage').value;

    // Формирование URL для запроса
    const url = `/api/cars/?brand=${brand}&price_from=${priceFrom}&price_to=${priceTo}&year_from=${yearFrom}&year_to=${yearTo}&mileage=${mileage}`;

    // Перенаправление на страницу с результатами поиска
    window.location.href = url;
}
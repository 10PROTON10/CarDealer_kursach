// Функция для запроса и отображения отсортированных машин
// const csrfToken = document.cookie
//     .split('; ')
//     .find(row => row.startsWith('csrftoken='))
//     .split('=')[1];
//
// // Функция для запроса и отображения отсортированных машин
// function sortFavoriteCars() {
//     const sortSelect = document.getElementById('sort-select');
//     const selectedSortMethod = sortSelect.value;
//
//     const token = localStorage.getItem('access_token');
//     console.log('Token:', token);
//
//     fetch(`/api/get_sorted_favorite_cars/${selectedSortMethod}/`, {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${token}`,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response:', data);
//
//         // Обновление страницы после получения отсортированных данных
//         renderCars(data);
//     })
//     .catch(error => console.error('Error:', error));
// }
//
// // Функция для отображения машин на странице
// function renderCars(data) {
//     const containerForCars = document.getElementById('container-for-cars');
//     containerForCars.innerHTML = '';  // Очистка текущего списка
//
//     data.forEach(favorite => {
//         const carContainer = document.createElement('div');
//         carContainer.classList.add('d-flex', 'car-container');
//
//         carContainer.innerHTML = `
//             <img class="car-image" src="${favorite.car.image}" alt="${favorite.car.model} Image">
//             <div class="car-details">
//                 <h3>${favorite.car.brand} ${favorite.car.model}</h3>
//                 <p>Year: ${favorite.car.year}</p>
//                 <p>Price: ${favorite.car.price}</p>
//                 <p>Description: ${favorite.car.description}</p>
//                 <p>Engine: ${favorite.car.engine}</p>
//                 <button class="remove-btn" onclick="removeFromFavorites(${favorite.car.id})">Remove</button>
//                 <button class="btn btn-primary" onclick="addToComparison(${favorite.car.id})">
//                     Добавить в сравнение
//                 </button>
//             </div>
//         `;
//
//         containerForCars.appendChild(carContainer);
//     });
// }
//
// function addToComparison(carId) {
//     const token = localStorage.getItem('access_token');
//     console.log('Token:', token);
//
//     fetch(`/api/add_to_comparison/${carId}/`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${token}`,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response:', data);
//     })
//     .catch(error => console.error('Error:', error));
// }
//
// // Функция для удаления машины из избранного
// function removeFromFavorites(carId) {
//     const token = localStorage.getItem('access_token');
//     console.log('Token:', token);
//
//     fetch(`/api/remove_from_favorites/${carId}/`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${token}`,
//             'X-CSRFToken': csrfToken,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response:', data);
//         // Проверяем успешность удаления
//         if (data.message === 'Машина удалена из избранного') {
//             // Вызываем функцию для обновления списка после успешного удаления
//             sortFavoriteCars();
//         } else {
//             console.error('Ошибка при удалении машины из избранного');
//         }
//     })
//     .catch(error => console.error('Error:', error));
// }
//
// // Начальная загрузка машин при открытии страницы
// document.addEventListener('DOMContentLoaded', () => {
//     // Загружаем избранные машины с дефолтной сортировкой
//     sortFavoriteCars();
// });



// Функция для запроса и отображения отсортированных машин
// const csrfToken = document.cookie
//     .split('; ')
//     .find(row => row.startsWith('csrftoken='))
//     .split('=')[1];
//
// // Функция для запроса и отображения отсортированных машин
// function sortFavoriteCars() {
//     const sortSelect = document.getElementById('sort-select');
//     const selectedSortMethod = sortSelect.value;
//
//     const token = localStorage.getItem('access_token');
//     console.log('Token:', token);
//
//     fetch(`/api/get_sorted_favorite_cars/${selectedSortMethod}/`, {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${token}`,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response:', data);
//
//         // Обновление страницы после получения отсортированных данных
//         renderCars(data);
//     })
//     .catch(error => console.error('Error:', error));
// }
//
// // Функция для отображения машин на странице
// function renderCars(data) {
//     const containerForCars = document.getElementById('container-for-cars');
//     containerForCars.innerHTML = '';  // Очистка текущего списка
//
//     data.forEach(favorite => {
//         const carContainer = document.createElement('div');
//         carContainer.classList.add('d-flex', 'car-container');
//
//         carContainer.innerHTML = `
//             <img class="car-image" src="${favorite.car.image}" alt="${favorite.car.model} Image">
//             <div class="car-details">
//                 <h3>${favorite.car.brand} ${favorite.car.model}</h3>
//                 <p>Year: ${favorite.car.year}</p>
//                 <p>Price: ${favorite.car.price}</p>
//                 <p>Mileage: ${favorite.car.mileage}</p>
//                 <p>Engine: ${favorite.car.engine}</p>
//                 <p>Engine Volume: ${favorite.car.engine_volume}</p>
//                 <p>Engine Power: ${favorite.car.engine_power}</p>
//                 <p>Transmission: ${favorite.car.transmission}</p>
//                 <p>Gears: ${favorite.car.gears}</p>
//                 <p>Drive: ${favorite.car.drive}</p>
//                 <p>Fuel Consumption: ${favorite.car.fuel_consumption}</p>
//                 <p>Body Type: ${favorite.car.body_type}</p>
//                 <button class="remove-btn" onclick="removeFromFavorites(${favorite.car.id})">Remove</button>
//                 <button class="btn btn-primary" onclick="addToComparison(${favorite.car.id})">
//                     Добавить в сравнение
//                 </button>
//             </div>
//         `;
//
//         containerForCars.appendChild(carContainer);
//     });
// }
//
// function addToComparison(carId) {
//     const token = localStorage.getItem('access_token');
//     console.log('Token:', token);
//
//     fetch(`/api/add_to_comparison/${carId}/`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${token}`,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response:', data);
//     })
//     .catch(error => console.error('Error:', error));
// }
//
// // Функция для удаления машины из избранного
// function removeFromFavorites(carId) {
//     const token = localStorage.getItem('access_token');
//     console.log('Token:', token);
//
//     fetch(`/api/remove_from_favorites/${carId}/`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${token}`,
//             'X-CSRFToken': csrfToken,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response:', data);
//         // Проверяем успешность удаления
//         if (data.message === 'Машина удалена из избранного') {
//             // Вызываем функцию для обновления списка после успешного удаления
//             sortFavoriteCars();
//         } else {
//             console.error('Ошибка при удалении машины из избранного');
//         }
//     })
//     .catch(error => console.error('Error:', error));
// }



// Функция для запроса и отображения отсортированных машин
const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    .split('=')[1];

// Функция для запроса и отображения отсортированных машин
function sortFavoriteCars() {
    const sortSelect = document.getElementById('sort-select');
    const selectedSortMethod = sortSelect.value;

    const token = localStorage.getItem('access_token');
    console.log('Token:', token);

    fetch(`/api/get_sorted_favorite_cars/${selectedSortMethod}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data);

        // Обновление страницы после получения отсортированных данных
        renderCars(data);
    })
    .catch(error => console.error('Error:', error));
}


// Пример API endpoint для получения информации о брендах
const brandApiEndpoint = '/api/brands';

// Создайте объект для хранения данных о брендах
const brandData = {};

// Запросите список брендов и сохраните его в brandData
fetch(brandApiEndpoint)
    .then(response => response.json())
    .then(data => {
        data.forEach(brand => {
            brandData[brand.id] = brand.name;
        });

        // Теперь у вас есть объект brandData с соответствиями id -> name
    })
    .catch(error => console.error('Error fetching brands:', error));

// Функция для получения имени бренда по его id
function getBrandName(brandId) {
    return brandData[brandId] || 'Unknown Brand';
}

async function renderCars(data) {
    const containerForCars = document.getElementById('container-for-cars');
    containerForCars.innerHTML = '';  // Очистка текущего списка

    // Дождитесь, пока будут загружены данные о брендах
    await fetch(brandApiEndpoint)
        .then(response => response.json())
        .then(brands => {
            brands.forEach(brand => {
                brandData[brand.id] = brand.name;
            });
        })
        .catch(error => console.error('Error fetching brands:', error));

    // Рендеринг машин
    data.forEach(favorite => {
        const carContainer = document.createElement('div');
        carContainer.classList.add('d-flex', 'car-container');

        const brandName = getBrandName(favorite.car.brand);

        carContainer.innerHTML = `
            <img class="car-image" src="${favorite.car.image}" alt="${favorite.car.model} Image">
            <div class="car-details">
                <h3>${brandName} ${favorite.car.model} - Year: ${favorite.car.year} - Price: ${favorite.car.price}</h3>
                <div class="row">
                    <div class="col-md-4">
                        <p>Mileage: ${favorite.car.mileage}</p>
                        <p>Engine: ${favorite.car.engine}</p>
                        <p>Engine Volume: ${favorite.car.engine_volume}</p>
                    </div>
                    <div class="col-md-4">
                        <p>Engine Power: ${favorite.car.engine_power}</p>
                        <p>Transmission: ${favorite.car.transmission}</p>
                        <p>Gears: ${favorite.car.gears}</p>
                    </div>
                    <div class="col-md-4">
                        <p>Drive: ${favorite.car.drive}</p>
                        <p>Fuel Consumption: ${favorite.car.fuel_consumption}</p>
                        <p>Body Type: ${favorite.car.body_type}</p>
                    </div>
                </div>
                <div class="d-flex justify-content-between align-items-end">
                    <button class="remove-btn" onclick="removeFromFavorites(${favorite.car.id})">
                        Remove
                    </button>
                    <button class="btn btn-primary" onclick="addToComparison(${favorite.car.id})">
                        Добавить в сравнение
                    </button>
                </div>
            </div>
        `;

        containerForCars.appendChild(carContainer);
    });
}

function addToComparison(carId) {
    const token = localStorage.getItem('access_token');
    console.log('Token:', token);

    fetch(`/api/add_to_comparison/${carId}/`, {
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

// Функция для удаления машины из избранного
function removeFromFavorites(carId) {
    const token = localStorage.getItem('access_token');
    console.log('Token:', token);

    fetch(`/api/remove_from_favorites/${carId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
            'X-CSRFToken': csrfToken,
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data);
        // Проверяем успешность удаления
        if (data.message === 'Машина удалена из избранного') {
            // Вызываем функцию для обновления списка после успешного удаления
            sortFavoriteCars();
        } else {
            console.error('Ошибка при удалении машины из избранного');
        }
    })
    .catch(error => console.error('Error:', error));
}


// Функция для отображения машин на странице
// const catalogBrand = [
//     { id: 1, name: 'Volkswagen' },
//     { id: 2, name: 'Subaru' },
//     { id: 3, name: 'Chevrolet' },
//     { id: 4, name: 'BMW' },
//     // Добавьте остальные бренды
// ];
//
// function renderCars(data) {
//     const containerForCars = document.getElementById('container-for-cars');
//     containerForCars.innerHTML = '';  // Очистка текущего списка
//
//     data.forEach(favorite => {
//         const carContainer = document.createElement('div');
//         carContainer.classList.add('d-flex', 'car-container');
//
//         // Находим соответствующий объект бренда в массиве catalog_brand
//         const brandObject = catalogBrand.find(brand => brand.id === favorite.car.brand);
//
//         carContainer.innerHTML = `
//             <img class="car-image" src="${favorite.car.image}" alt="${favorite.car.model} Image">
//             <div class="car-details">
//                 <h3>${brandObject ? brandObject.name : 'Unknown Brand'} ${favorite.car.model} - Year: ${favorite.car.year} - Price: ${favorite.car.price}</h3>
//                 <div class="row">
//                     <div class="col-md-6">
//                         <p>Mileage: ${favorite.car.mileage}</p>
//                         <p>Engine: ${favorite.car.engine}</p>
//                         <p>Engine Volume: ${favorite.car.engine_volume}</p>
//                         <p>Engine Power: ${favorite.car.engine_power}</p>
//                     </div>
//                     <div class="col-md-6">
//                         <p>Transmission: ${favorite.car.transmission}</p>
//                         <p>Gears: ${favorite.car.gears}</p>
//                         <p>Drive: ${favorite.car.get_drive_display}</p>
//                         <p>Fuel Consumption: ${favorite.car.fuel_consumption}</p>
//                         <p>Body Type: ${favorite.car.body_type}</p>
//                     </div>
//                 </div>
//                 <div class="d-flex justify-content-between align-items-end">
//                     <button class="remove-btn" onclick="removeFromFavorites(${favorite.car.id})">
//                         Remove
//                     </button>
//                     <button class="btn btn-primary" onclick="addToComparison(${favorite.car.id})">
//                         Добавить в сравнение
//                     </button>
//                 </div>
//             </div>
//         `;
//
//         containerForCars.appendChild(carContainer);
//     });
// }




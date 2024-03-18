$(document).ready(function () {
    var $carousel = $('.car-carousel');
    var $checkbox = $('#show-differences');

    $carousel.slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        prevArrow: '<button type="button" class="slick-prev">&#9664;</button>',
        nextArrow: '<button type="button" class="slick-next">&#9654;</button>',
        infinite: false,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    $('.left-arrow').on('click', function () {
        $carousel.slick('slickPrev');
        updateComparisonView();
    });

    $('.right-arrow').on('click', function () {
        $carousel.slick('slickNext');
        updateComparisonView();
    });

    $checkbox.on('change', function () {
        updateComparisonView();
    });

    $('.remove-icon').on('click', function () {
        var carId = $(this).data('car-id');
        removeCarFromComparison(carId);
    });

    function updateComparisonView() {
        var showDifferences = $checkbox.prop('checked');

        if (showDifferences) {
            compareAndHide();
        } else {
            $('.card-text').show();
        }
    }

    function compareAndHide() {
        var characteristicValues = {};

        $('.card-text').each(function () {
            var $currentCardText = $(this);
            var currentCharacteristic = $currentCardText.data('characteristic');
            var currentValue = $currentCardText.text().trim();

            if (!characteristicValues[currentCharacteristic]) {
                characteristicValues[currentCharacteristic] = new Set();
            }

            characteristicValues[currentCharacteristic].add(currentValue);
        });

        $('.card-text').each(function () {
            var $currentCardText = $(this);
            var currentCharacteristic = $currentCardText.data('characteristic');
            var currentValue = $currentCardText.text().trim();

            if (characteristicValues[currentCharacteristic].size === 1) {
                $currentCardText.hide();
            } else {
                $currentCardText.show();
            }
        });
    }
});




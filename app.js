// static/app.js
function generateFacade() {
    const width = document.getElementById('width').value;
    const height = document.getElementById('height').value;
    const glassType = document.getElementById('glassType').value;
    const windowCount = document.getElementById('windowCount').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `width=${width}&height=${height}&glassType=${glassType}&windowCount=${windowCount}`,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('facadeContainer').innerHTML = data.facade_svg;

        // You can use the window_positions data to allow users to edit window positions later
        console.log('Window Positions:', data.window_positions);
    });
}

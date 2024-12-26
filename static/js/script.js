//function loadContent(url) {
//    fetch(url)
//        .then(response => {
//            if (!response.ok) {
//                throw new Error('Failed to load content');
//            }
//            return response.text();
//        })
//        .then(data => {
//            document.getElementById('content-area').innerHTML = data;
//        })
//        .catch(error => {
//            console.error('Error loading content:', error);
//            document.getElementById('content-area').innerHTML = '<p>Error loading content. Please try again.</p>';
//        });
//}


function loadContent(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load content');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('content-area').innerHTML = data;

            // Trigger MathJax re-rendering
            if (window.MathJax) {
                MathJax.typesetPromise()
                    .then(() => {
                        console.log('MathJax rendering completed.');
                    })
                    .catch((err) => {
                        console.error('MathJax rendering failed:', err);
                    });
            } else {
                console.warn('MathJax is not loaded.');
            }
        })
        .catch(error => {
            console.error('Error loading content:', error);
            document.getElementById('content-area').innerHTML = '<p>Error loading content. Please try again.</p>';
        });
}

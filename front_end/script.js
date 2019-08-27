const converter = new showdown.Converter()

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
    do {
        fetch('/README.md').then(response => {
            return response.text()
        }).then(function(markdown) {
            document.getElementById('talk')
                .innerHTML = converter.makeHtml(markdown);
        });
        await sleep(10000);
    } while ( true );
}
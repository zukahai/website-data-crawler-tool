document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('startButton').addEventListener('click', function() {
    start()
  });

  document.getElementById('stopButton').addEventListener('click', function() {
    // Có thể thêm chức năng dừng ở đây (nếu có)
  });
});

function start() {
  // await loadUrl('https://drive.base.vn');
  console.log('loaded: ', 'https://drive.base.vn');
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    console.log(tabs);
    if (tabs.length > 0) {
      chrome.tabs.executeScript(tabs[0].id, { code: 'document.documentElement.outerHTML' }, function(html) {
        console.log(html);
        console.log(html[0]); // Mã HTML của trang hiện tại sẽ được log ra console
      });
    }
  });
  
}

function crawl() {
  let table = [];
    // Lấy tất cả các div có class là 'js-folders'
    const folders = document.querySelectorAll('.js-folders');

    console.log('length: ', folders.length);

    // Duyệt qua mỗi div có class 'js-folders'
    folders.forEach(folder => {
        // Tìm tất cả các phần tử có class 'name' bên trong div hiện tại
        const nameElements = folder.querySelectorAll('.name');

        // Lặp qua từng phần tử 'name' trong div hiện tại
        nameElements.forEach(nameElement => {
            // Tìm thẻ span bên trong phần tử 'name' hiện tại
            const spanWithDataXurl = nameElement.querySelector('span[data-xurl]');

            if (spanWithDataXurl) {
                const dataXurl = spanWithDataXurl.getAttribute('data-xurl');
                const nameContent = nameElement.textContent.trim();

                console.log(nameContent + " " + dataXurl);
                // Hoặc có thể thực hiện các thao tác khác với cả hai giá trị ở đây
                table.push({
                    name: nameContent,
                    url: domain + dataXurl
                })
            }
        });
    });

    table.forEach(item => {
        //thêm vào thẻ div có id là content
        const content = document.getElementById('content');
        content.innerHTML += `<a href="${item.url}">${item.name}</a><br>`
    })
}



async function loadUrl(url) {
  new Promise((resolve, reject) => {
    chrome.tabs.create({ url: 'https://drive.base.vn' });
    setTimeout(() => {
      console.log('loaded: ', url);
      resolve();
    }, 2000);
  })
}

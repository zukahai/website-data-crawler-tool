const fs = require("fs");
const axios = require("axios");
const { log } = require("console");
const { Parser } = require('json2csv');

const queue = [];
const results = [];
const callApi = async (data, id, page) => {
    let url = 'https://drive.base.vn/thanhphong1110-drive'
    if (id !== -1)
        url += '/folder/' + id
    url += '?page=' + page
    const response = await axios.post(url, data, {
        headers: {
            "accept": "*/*",
            "accept-language": "vi,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"YaBrowser\";v=\"23\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",

        },
        responeEncoding: "utf-8",
        // Thêm các tùy chọn khác ở đây (nếu cần)
    })
    if (response.data) {
        const jsonData = response.data._page_data;
        const regexPattern = /Client\.pageData=(\{.*\});/;

        const match = jsonData.match(regexPattern);

        if (match) {
            const clientPageDataStr = match[1];

            const clientPageData = JSON.parse(clientPageDataStr);

            // fs.writeFileSync("./data/" + id + ".json", JSON.stringify(clientPageData));
            return clientPageData
        } else {
            return null
        }
    }
}

(async () => {
    const config = JSON.parse(fs.readFileSync('./config.json', 'utf8'));
    queue.push({
        index: "",
        id: -1,
        name: "root",
    })
    let count = 0;
    while (queue.length) {
        const q = queue.shift();
        const folderResult = 'results'
        if (!fs.existsSync(folderResult)) {
            fs.mkdirSync(folderResult);
        }
        fs.writeFileSync(`./${folderResult}/results.json`, JSON.stringify(results));

        log(++count + '/' + results.length + "\t" + q.id + " - " + q.name)

        let page = 1;
        let folders = [];
        let index = 1;
        do {
            const data = await callApi(config, q.id, page++);
            folders = data.folders;
            for (const item of folders) {
                const date = new Date(item.last_update * 1000);
                const formattedDate = `${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}:${('0' + date.getSeconds()).slice(-2)} ${('0' + date.getDate()).slice(-2)}/${('0' + (date.getMonth() + 1)).slice(-2)}/${date.getFullYear() % 100}`;
                const subForder = {
                    index: q.index + index++ + ".",
                    stt: results.length + 1,
                    id: item.id,
                    name: item.name,
                    link: 'https://drive.base.vn/thanhphong1110-drive/folder/' + item.id,
                    files: item.stats.files,
                    folders: item.stats.folders,
                    lastUpdate: formattedDate,
                    isFile: false,
                    linkFile: ""
                }
                results.push(subForder)
                queue.push(subForder)
            }

            files = data.files;
            for (const item of files) {
                const date = new Date(item.since * 1000);
                const formattedDate = `${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}:${('0' + date.getSeconds()).slice(-2)} ${('0' + date.getDate()).slice(-2)}/${('0' + (date.getMonth() + 1)).slice(-2)}/${date.getFullYear() % 100}`;
                const subForder = {
                    index: q.index + index++ + ".",
                    stt: results.length + 1,
                    id: item.id,
                    name: item.preview.name,
                    link: 'https://drive.base.vn/thanhphong1110-drive/folder/' + q.id,
                    files: 0,
                    folders: 0,
                    lastUpdate: formattedDate,
                    isFile: true,
                    linkFile: item.preview.url

                }
                results.push(subForder)
                log(++count + '/' + results.length + "\t" + item.preview.name)
            }
        } while (folders.length > 0)
    }
    json_to_csv(results);

})();

const conpare = (a, b) => {
    const arrA = a.split('.');
    const arrB = b.split('.');
    for (let i = 0; i < Math.min(arrA.length, arrB.length); i++) {
        if (arrA[i] !== arrB[i]) {
            return Math.floor(arrA[i] )- Math.floor(arrB[i]);
        }
    }
    return arrA.length - arrB.length;
}

const json_to_csv = (data) => {
    const folderResult = 'results'
    if (!fs.existsSync(folderResult)) {
        fs.mkdirSync(folderResult);
    }
    const jsonData = data

    // sắp xếp data theo index
    jsonData.sort((a, b) => {
        return conpare(a.index, b.index);
    })

    const fields = ['index', 'stt', 'id', 'name', 'link', 'files', 'folders', 'lastUpdate', 'isFile', 'linkFile'];

    const json2csvParser = new Parser({ fields });
    const csv = json2csvParser.parse(jsonData);

    fs.writeFileSync(`./${folderResult}/result.csv`, '\uFEFF' + csv, 'utf8');
    console.log('Tệp CSV đã được tạo');
}

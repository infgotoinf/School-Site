const fs = require('fs');
const readline = require('readline');
const simpleGit = require('simple-git');
const git = simpleGit();

// 1. Функция сохранения таблицы в JSON файл и отправка на GitHub
async function save(database, filename) {
    fs.writeFileSync(filename, JSON.stringify(database, null, 2));
    console.log(`Файл ${filename} сохранён.`);

    try {
        await git.add(filename);
        await git.commit(`Update ${filename}`);
        await git.push();
        console.log(`Файл ${filename} отправлен на GitHub.`);
    } catch (err) {
        console.error("Ошибка при отправке на GitHub:", err);
    }
}

// 1. Функция импорта JSON таблицы в переменную
function importData(filename) {
    if (fs.existsSync(filename)) {
        const data = fs.readFileSync(filename);
        return JSON.parse(data);
    } else {
        console.log(`Файл ${filename} не найден.`);
        return [];
    }
}

// 2. Функция вывода таблицы
function printTable(database) {
    if (database.length === 0) {
        console.log("Таблица пуста.");
        return;
    }

    const headers = Object.keys(database[0]);
    console.log(headers.join('\t|\t'));
    console.log('-'.repeat(50));

    database.forEach(row => {
        const values = headers.map(header => row[header] || '');
        console.log(values.join('\t|\t'));
    });

    console.log('-'.repeat(50));
}

// 2. Функция создания новой таблицы
async function createTable() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise(resolve => rl.question(query, resolve));

    const tableName = await question("ENTER THE NAME OF NEW TABLE: ");
    const allParams = [];

    console.log("Введите параметры таблицы (оставьте пустым для завершения):");
    while (true) {
        const param = await question("ENTER THE NAME OF NEW PARAMETER: ");
        if (param.trim() === '') break;
        allParams.push(param);
    }

    const table = [];

    let addMore = true;
    while (addMore) {
        const newRow = {};
        for (const param of allParams) {
            const value = await question(`ENTER ${param}: `);
            newRow[param] = value;
        }
        table.push(newRow);

        const more = await question("Добавить ещё строку? (y/n): ");
        addMore = more.trim().toLowerCase() === 'y';
    }

    rl.close();
    await save(table, `../files/tables/${tableName}.json`);

    // Добавление названия новой таблицы в AllDataDatabase.json
    const allDataDatabase = importData('AllDataDatabase.json');
    allDataDatabase.push({ name: `${tableName}.json` });
    await save(allDataDatabase, 'AllDataDatabase.json');

    return table;
}

// 3. Функция добавления элемента в таблицу
async function addElement(database, tableName) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise(resolve => rl.question(query, resolve));

    const newRow = {};
    const headers = Object.keys(database[0]);
    for (const header of headers) {
        const value = await question(`ENTER ${header}: `);
        newRow[header] = value;
    }

    database.push(newRow);
    await save(database, `${tableName}.json`);
    rl.close();
}

// 3. Функция удаления элемента по индексу
async function deleteElement(database, tableName) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise(resolve => rl.question(query, resolve));

    const idx = await question("ENTER INDEX OF AN ELEMENT TO DELETE: ");
    if (database[idx]) {
        database.splice(idx, 1);
        await save(database, `${tableName}.json`);
        console.log("Элемент удалён.");
    } else {
        console.log("Элемент с таким индексом не найден.");
    }

    rl.close();
}

// Основное меню
async function mainMenu() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    const question = (query) => new Promise(resolve => rl.question(query, resolve));

    while (true) {
        const action = await question("ENTER: [1] TO PRINT A TABLE; [2] TO CREATE A TABLE; [3] TO EXIT\n");

        switch (action.trim()) {
            case '1':
                const allData = importData('AllDataDatabase.json');
                if (allData.length === 0) {
                    console.log("Нет доступных таблиц.");
                    break;
                }

                console.log("Доступные таблицы:");
                allData.forEach((file, idx) => console.log(`${idx + 1}. ${file.name}`));

                const tableName = await question("Введите название таблицы для открытия (без .json): ");
                const database = importData(`../files/tables/${tableName}.json`);

                if (database.length === 0) {
                    console.log("Таблица пуста или не существует.");
                    break;
                }

                printTable(database);

                const action2 = await question("WHAT DO YOU WANT? [1] ADD ELEMENT; [2] DELETE ELEMENT\n");
                switch (action2.trim()) {
                    case '1':
                        await addElement(database, tableName);
                        break;
                    case '2':
                        await deleteElement(database, tableName);
                        break;
                    default:
                        console.log("Некорректный выбор.");
                        break;
                }
                break;

            case '2':
                await createTable();
                break;

            case '3':
                rl.close();
                return;

            default:
                console.log("Некорректный ввод. Попробуйте снова.");
        }
    }
}

// Запуск программы
mainMenu();

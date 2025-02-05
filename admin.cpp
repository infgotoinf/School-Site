#include <windows.h>
#include <filesystem>
#include <fstream>
#include "nlohmann/json.hpp"
#include <iostream>
#include <vector>

namespace fs = std::filesystem;
using std::string;
using nlohmann::json;
using std::vector;

HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 1 Функция сохранения таблицы в json файл
void save(json const Database, string filename)
{
	std::ofstream file(filename);
	file << Database;
	// ЕСЛИ ВОЗМОЖНО, НУЖНО ЧТОБЫ ПОСЛЕ СОХРАНЕНИЯ ДАННЫХ, ОНИ ОТПРАВЛЯЛИСЬ НА ГИТХАБ
}

// 1 Функция импорта json таблицы в переменную
void import(json& Database, string filename)
{
	std::ifstream database(filename);
	database >> Database;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 2 Функция вывода таблицы
void print(json const Database)
{
	// Вывод названий столбцов в виде таблицы
	for (auto param : Database[0]){
		std::cout << "|" << (string)param << "\t\t\t";
	}
	// Разделитель
	std::cout << "---------------------------------------------------------------------------------------------------";
	
	// Вывод элементов таблицы по столбцам
	for (int i = 0; i < Database.size(); i++)
	{
		for (auto param : Database[i]){
			std::cout << "|" << Database[param] << "\t\t\t";
		}
	}
	std::cout << "---------------------------------------------------------------------------------------------------";
}

// 2 Функция создания новой таблицы
json create() {
	string table_name;
	std::cout << "ENTER THE NAME OF NEW TABLE: ";
	std::cin >> table_name;
	
	string param;
	string attribute;
	vector<string> all_param;
	json table;

	// Ввод названий параметров таблицы пока пользователь не захочет уйти
	std::cin >> param;
	while (param != " ")
	{
		std::cout << "ENTER THE NAME OF NEW PARAMETER: ";
		all_param.push_back(param);
		std::cin >> param;
	} 
	
	// Добавление нулевого элемента в таблицу
	for (auto param : all_param)
	{
		std::cout << "ENTER " << (string)param << ": ";
		std::cin >> attribute;
		// ТУТ ДОЛЖНА ПРОИСХОДИТ ЗАПИСЬ ДАННЫХ В JSON
	}
	return table;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 3 Функция удаления элемента по индексу
void DeleteElem(json &Database)
{
	int idx;
	std::cout << "ENTER INDEX OF AN ELEMENT: ";
	std::cin << idx;
	Database[idx].clear();
}

// 3 Функция создания нового элемента в таблице
void AddElem(json &Database)
{
	string attribute;
	Database.push_back();
	for (auto param : Database[0]) {
		std::cout << "ENTER " << (string)param << ": ";
		std::cin << attribute;
		Database.back()[param] = attribute;
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main() {
	setlocale(0, "");

	// 1 При запуске показывается меню с выбором действия
	menu:
	int action;
	std::cout << "ENTER: [1] TO PRINT A TABLE; [2] TO CREATE A TABLE\n";
	std::cin >> action;


	// 1 В зависимости от выбранного действия запускается функция
	system("cls");
	switch (action)
	{
		case 1:
			// AllDataDatabase.json должен содержать в себе названия всех существующих таблиц
			json AllDataDatabase;
			import(AllDataDatabase, "AllDataDatabase.json");

			// Происходит вывод названия всех существующих таблиц
			for (auto file : AllDataDatabase) {
				std::cout << file["name"] << '\n';
			}

			// Пользователь вводит название таблицы которую хочет изменить
			string Databasename;
			std::cin >> Databasename;
			json Database;
			import(Database, Databasename);

			print(Database); // Таблица выводится

			// Пользователя спрашивают что он хочет сделать
			int action2;
			std::cout << "WHAT DO YOU WANT? [1] ADD ELEMENT; [2] DELETE ELEMENT\n";
			std::cin >> action2;
			switch (action2)
			{
				case 1:
					AddElem(Database);
				case 2:
					DeleteElem(Database);
			}
			save(Database, Databasename);  // БД сохраняется
			break;
		case 2:
			Database = create();
			// СОЗДАЁТСЯ СООТВЕТСТВУЮЩИЙ ФАЙЛ И СОХРАНЯЕТСЯ
			break;
	}
	goto menu;
	
	return 0;
}
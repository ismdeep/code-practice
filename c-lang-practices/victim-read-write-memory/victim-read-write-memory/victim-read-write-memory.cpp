// victim-read-write-memory.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <TlHelp32.h>
#include <string.h>
#include <string>
#include <iostream>

#pragma comment(lib, "Shlwapi")

using namespace std;

DWORD FindProcessId(const std::wstring& processName)
{
	PROCESSENTRY32 processInfo;
	processInfo.dwSize = sizeof(processInfo);
	HANDLE processesSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);
	if (processesSnapshot == INVALID_HANDLE_VALUE)
		return 0;

	Process32First(processesSnapshot, &processInfo);
	if (!processName.compare(processInfo.szExeFile))
	{
		CloseHandle(processesSnapshot);
		return processInfo.th32ProcessID;
	}

	while (Process32Next(processesSnapshot, &processInfo))
	{
		if (!processName.compare(processInfo.szExeFile))
		{
			CloseHandle(processesSnapshot);
			return processInfo.th32ProcessID;
		}
	}

	CloseHandle(processesSnapshot);
	return 0;
}


int _tmain(int argc, _TCHAR* argv[])
{
	LPCVOID address = (LPCVOID)0x000000000022FE45;
	char buffer[64];
	DWORD processId = FindProcessId(L"simple_while_print.exe");
	HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, 0, processId);
	ReadProcessMemory(hProcess, address, &buffer, sizeof(buffer), 0);
	cout << "Data read from remote process: " << buffer << endl;
	DWORD dwNumberOfBytesRead;
	char buffer2[] = "hacked!\0\0";
	WriteProcessMemory(hProcess, (LPVOID)address, buffer2, strlen(buffer2) + 2, &dwNumberOfBytesRead);

	system("pause");
	return 0;
}


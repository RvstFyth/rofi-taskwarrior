#!/usr/bin/env python

import os
import json
import subprocess
import sys


def main():
    if len(sys.argv) == 1:
        task_new()
        #list_tasks()
    else:
        if len(sys.argv) > 2:
            method = sys.argv[1]
            task_id = sys.argv[2]
            if method == 'delete':
                task_delete(task_id)
            elif method == 'done':
                task_done(task_id)
        elif len(sys.argv) == 2 and sys.argv[1] == 'list':
            list_tasks()


def load_tasks(limit=5):
    tasks = subprocess.check_output("task 1-"+str(limit)+" export", shell=True)
    tasks_parsed = json.loads(tasks)
    return tasks_parsed


def list_tasks():
    tasks = load_tasks(50)
    tmp = ''
    for task in tasks:
        tmp += '{} {}|'.format(task['id'], task['description'])

    tmp = tmp[:-1]
    selected = subprocess.getoutput("echo '" + tmp + "' | rofi -sep '|' -dmenu -p 'Tasks'")
    if selected != '':
        selected_index = int(selected.split(" ")[0])
        selected_task = tasks[selected_index - 1]
        task_done(selected_task)


def task_new():
    new_task = subprocess.getoutput('rofi -dmenu -input /dev/null -p "Task " -lines 0')
    result = subprocess.getoutput("task add " + str(new_task))
    os.system("rofi -e '{}'".format(result))


def task_done(task):
    os.system("task {} done".format(task['id']))
    os.system("rofi -e '{} marked as completed'".format(task['description']))


def task_delete(task_id):
    print(task_id)


if __name__ == "__main__":
    main()


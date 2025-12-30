def main():
    full_name = "Наконечная Анастасия Евгеньевна"
    group_number = "М1125-38.04.05фт"
    
    print("=" * 60)
    print(f"ФИО: {full_name}")
    print(f"Номер группы: {group_number}")
    print("-" * 60)
    
    import datetime
    import sys
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    python_version = sys.version.split()[0]
    
    print(f"Время выполнения: {current_time}")
    print(f"Версия Python: {python_version}")
    print("=" * 60)

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
from src.functions import *

try:
    # Крок 1
    data = list(map(read_dataset,
        [ 'Time 0.txt'
        , 'Time 21 hours.txt'
        , 'Time 48 hours.txt'
    #   , '181213_A1.sca'
        ]))

    # Крок 2
    data = list(map(filter_dataset, data))

    steps = [dataset.step for dataset in data]
    if not check_wavestep(steps):
        data = [
            normalize_wavestep(max(steps), dataset)
            for dataset in data
        ]

    # Крок 3
    for dataset in data:
        plt.plot(dataset.length, dataset.absorption, label=dataset.label)

    # plt.grid(axis='both')
    plt.minorticks_on()
    plt.grid(which='major', color = 'k')
    plt.grid(which='minor', color = 'k', linestyle = ':')

    plt.legend()
    plt.xlabel('wavelength')
    plt.ylabel('absorption')

    # plt.savefig('data')
    plt.show()

    # Крок 4
    table = []
    for dataset in data:
        max_al, max_a = get_max_absorption(dataset)
        table.append([dataset.label, max_al, max_a])

    for row in table:
        print(row)

    # Крок 5
    for i in range(len(data)):
        integral_absorption = get_integral_absorption(data[i])
        table[i].append(integral_absorption)

    print()
    for row in table:
        print(row)

    # Крок 6
    for i in range(len(data)):
        plt.plot\
            ( data[i].length
            , data[i].absorption
            , label=f'{ data[i].label }, S = { round(table[i][3]) }'
            , color=f'C{ i }'
            )
        plt.plot\
            ( table[i][1]
            , table[i][2]
            , marker='o'
            , color=f'C{ i }'
            )
        plt.text\
            ( table[i][1] * 1.01
            , table[i][2] * 1.01
            , f'({ table[i][1] }, { round(table[i][2], 2) })'
            )

    # plt.grid(axis='both')
    plt.minorticks_on()
    plt.grid(which='major', color = 'k')
    plt.grid(which='minor', color = 'k', linestyle = ':')
    plt.legend()
    plt.xlabel('wavelength')
    plt.ylabel('absorption')

    plt.savefig('data')
    plt.show()

    # Зсув піку свідчить про нестабільність розчинів.
    # Зниження інтегрального поглинання – про випадання наночастинок в осад.

    # Крок 7
    # Пік показника поглинання майже не зсувається, тобто розчини стабільні?
    # Інтегральне поглинання спочатку зменшується, потім дещо збільшується.

except Exception as e:
    print(e)

use std::fs::File;
use std::io::Read;

fn parse_file() -> String {
    let mut output: String = "".to_string();
    let mut input_file = File::open("input.txt").unwrap();
    input_file.read_to_string(&mut output).unwrap();
    output
}

fn get_seeds(file_input: &str) -> Vec<i128> {
    file_input.split("seeds: ").collect::<Vec<&str>>()[1]
        .split("\n\n")
        .collect::<Vec<&str>>()[0]
        .split(" ")
        .collect::<Vec<&str>>()
        .into_iter()
        .map(|x| x.parse::<i128>().unwrap())
        .collect::<Vec<i128>>()
}

fn get_map<'a, 'b>(file_input: &'a str, map_string: &'b str) -> Vec<Vec<&'a str>> {
    file_input.split(map_string).collect::<Vec<_>>()[1]
        .split("\n\n")
        .collect::<Vec<_>>()[0]
        .split("\n")
        .collect::<Vec<_>>()
        .into_iter()
        .map(|x| x.split(" ").collect::<Vec<_>>())
        .filter(|x| x.len() > 1)
        .collect::<Vec<_>>()
}

fn main() {
    let raw_file = parse_file();
    let seeds = get_seeds(&raw_file);
    let seed_soil = get_map(&raw_file, "seed-to-soil map:\n");
    let soil_fertilizer = get_map(&raw_file, "soil-to-fertilizer map:\n");
    let fertilizer_water = get_map(&raw_file, "fertilizer-to-water map:\n");
    let water_light = get_map(&raw_file, "water-to-light map:\n");
    let light_temperature = get_map(&raw_file, "light-to-temperature map:\n");
    let temperature_humidity = get_map(&raw_file, "temperature-to-humidity map:\n");
    let humidity_location = get_map(&raw_file, "humidity-to-location map:\n");

    let map_vec = vec![
        &seed_soil,
        &soil_fertilizer,
        &fertilizer_water,
        &water_light,
        &light_temperature,
        &temperature_humidity,
        &humidity_location,
    ];
    println!("{:?}", seeds);

    for mut i in 0.. {
        // println!("{}", i); Add to reveal the secrets of the universe
        for j in map_vec.iter().rev() {
            let mut matched = false;
            for k in j.iter() {
                let predicted =
                    -(k[0].parse::<i128>().unwrap() - k[1].parse::<i128>().unwrap() - i);
                if predicted >= k[1].parse::<i128>().unwrap()
                    && predicted < k[1].parse::<i128>().unwrap() + k[2].parse::<i128>().unwrap()
                    && !matched
                {
                    i = predicted;
                    matched = true;
                }
            }
        }
        for j in (0..seeds.len()).step_by(2) {
            if i >= seeds[j] && i <= seeds[j] + seeds[j + 1] {
                println!("{}", i);
                return;
            }
        }
    }
}

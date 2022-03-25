function solution(genres, plays) {
  var answer = [];

  const countMap = new Map();
  const genreMap = new Map();

  for (let i = 0; i < genres.length; i++) {
    if (countMap.has(genres[i])) {
      countMap.set(genres[i], countMap.get(genres[i]) + plays[i]);
    } else {
      countMap.set(genres[i], plays[i]);
    }
  }

  const genreSet = new Set(genres);
  for (genre of genreSet) {
    genreMap.set(genre, []);
  }

  genres.forEach((genre, index) => {
    genreMap.get(genre).push([plays[index], index]);
  });

  const popularGenres = Array.from([...countMap]).sort((a, b) => b[1] - a[1]);

  for (const info of popularGenres) {
    const genre = info[0];
    const songs = genreMap.get(genre);
    songs.sort((a, b) => {
      if (a[0] === b[0]) return a[1] - b[1];
      else return b[0] - a[0];
    });

    songs.slice(0, 2).forEach((song) => {
      answer.push(song[1]);
    });
  }

  return answer;
}

console.log(
  solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
  )
);

// console.log(
//   solution(
//     ["a", "b", "c", "d", "a", "d", "d", "d", "a", "a", "c", "c"],
//     [100, 300, 400, 150, 100, 300, 200, 600, 700, 110, 900, 9000]
//   )
// );

let BANNED_WORDS = [];

// Changes banned words in the message to stars (*)
async function filterBannedWords(message) {
  const success = await fetchBannedWords();

  if (success) {
    for(let i = 0; i < BANNED_WORDS.length - 1; i++) {
      const bannedWord = BANNED_WORDS[i];

      const replacement = '*'.repeat(bannedWord.length);
      message = message.replace(bannedWord, replacement);
    }
  }

  return message;
}

// Fetches banned words from a web endpoint, returns true if successful
async function fetchBannedWords() {
  const url = 'https://bannedwords.com/api/en/words?pages=all';
  const httpResponse = await fetch(url);

  if (httpResponse.ok) {
    const parsed = await httpResponse.json();

    BANNED_WORDS = parsed.words;
    return true;
  } else if (httpResponse.status == 500) {
    console.log('Response too large, it is timing out again...');
  }

  return false;
}



filterBannedWords("hello motherfucker")

//changes to be made:
//BANNED_WORDS.length - 1 => BANNED_WORDS.length
//replace => replaceAll
//BANNED_WORDS declared inside filterBannedWords() and passed to fetchBannedWords() directly
//use parsed.words.split(" ") to populate BANNED_WORDS into an array instead of plain JSON object
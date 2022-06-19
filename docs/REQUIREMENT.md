## Requirements of the assignment

Following is the example data structure for `episode`

```
{
  "id": "9b81efb6-e8a1-11ec-9e1d-eb36b3ac7ec2",
  "episodeTitle": "Economics 101",
  "podcastTitle": "Money and Fame",
  "thumbnailUrl": "https://example.com/somethumbnail.png",
  "guests": [
    {
      "name": "Adam Smith"
    },
    {
      "name": "Karl Marx"
    }
  ],
  "audioUrl": "https://example.com/episode_economics_101.mp3",
  "episodeDurationSeconds": 2100
}
```

- Write an HTTP endpoint to create an episode
- Write an HTTP endpoint to fetch an episode
- Write an HTTP endpoint to fetch all episodes
- Write an HTTP endpoint to delete an episode
- Add HTTP basic authentication on all of the above endpoints
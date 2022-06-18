from uuid import uuid4


def generate_test_dataset():
    """
    Generate 100 episodes to save in the test database
    """
    result = []

    for n in range(1, 101):
        num_in_str = str(n)

        payload = dict(
            id=uuid4(),
            episodeTitle=f"Episode title {num_in_str}",
            podcastTitle=f"Podcast title {num_in_str}",
            thumbnailUrl=f"https://example.com/somethumbnail_{num_in_str}.png",
            guests=[dict(name="Guest 1"), dict(name="Guest 2")],
            audioUrl=f"https://example.com/episode_{num_in_str}.mp3",
            episodeDurationSeconds=2100,
        )

        result.append(payload)

    return result

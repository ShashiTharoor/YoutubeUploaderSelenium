import Uploader 


YouTubeUploader=Uploader.YouTubeUploader()

def main(title,description,video_path)
    YouTubeUploader.UPLOADER(title, description, video_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video",
                        help='Path to the video file',
                        required=True)
    parser.add_argument("--title",
                        help='title',
                        required=True)
    parser.add_argument("--description",
                        help='description',
                        required=True)
    
    args = parser.parse_args()
    main(args.title, args.description, args.video)

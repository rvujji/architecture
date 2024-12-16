import React from "react";

// Define the type for the props
type VideoProps = {
  src: string; // The source of the video is a string
  controls?: boolean; // Controls are optional and default to true
};

const Video: React.FC<VideoProps> = ({ src, controls = true }) => {
  return (
    <div className="video-container">
      <video src={src} controls={controls} style={{ maxWidth: "100%" }} />
    </div>
  );
};

export default Video;

import React from 'react';

import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Popover from '@mui/material/Popover';

import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';

import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';

import Slider from '@mui/material/Slider';

import Typography from '@mui/material/Typography';

import FastRewind from '@mui/icons-material/FastRewind';
import FastForward from '@mui/icons-material/FastForward';
import PlayArrow from '@mui/icons-material/PlayArrow';
import Pause from '@mui/icons-material/Pause';
import VolumeUp from '@mui/icons-material/VolumeUp';
import Settings from '@mui/icons-material/Settings';

import { Duration } from "luxon";


export default class MultimediaPlayer extends React.Component {  
    constructor(props) {
        super(props);

        this.multimedia = null;

        this.volume_button= undefined;
        this.playback_speed_button = undefined;

        this.state = {
            is_playing: false, // check whether the user is playing the audio
            seeker_time: 0, // The time of the seeker
            seeker_max_value: 0, // Max value of the seeker
            duration: 0, // The duration of the audio for the seeker
            playback_speed: 1, // the speed of the player
            volume: 50, // the volume of the player
            time_skip_unit: 5, // the unit of time skipped for fast forwarding and rewinding
            
            is_volume_visible: false, // the visibility of the volume pop-over
            is_playback_speed_visible: false // the visibility of the playback speed popover
        }
    }

    componentDidMount() {
        this.multimedia.addEventListener('loadedmetadata', () => {
            this.setState({
                seeker_time: this.multimedia.currentTime,
                duration: this.multimedia.duration,
                volume: this.multimedia.volume,
                playback_speed: this.multimedia.playbackRate
            });
        });

        this.multimedia.addEventListener('play', () => {
            this.setState({
                is_playing: true
            });
        });

        this.multimedia.addEventListener('pause', () => {
            this.setState({
                is_playing: false
            });
        });

        this.multimedia.addEventListener('timeupdate', () => {
            this.setState({
                seeker_time: this.multimedia.currentTime
            });
        });

        this.multimedia.addEventListener('volumechange', () => {
            this.setState({
                volume: this.multimedia.volume
            });
        });

        this.multimedia.addEventListener('ratechange', () => {
            this.setState({
                playback_speed: this.multimedia.playbackRate
            });
        });
    }

    toggleVolumeVisibility = () => {
        this.setState({
            is_volume_visible: !this.state.is_volume_visible
        });
    }

    togglePlaybackSpeedVisibility = () => {
        this.setState({
            is_playback_speed_visible: !this.state.is_playback_speed_visible
        });
    }

    toggleMediaPlayback = () => {
        if (!this.state.is_playing) {
            this.playMedia();
         } else this.pauseMedia();
    }

    playMedia = () => {
        this.multimedia.play();
    }

    pauseMedia = () => {
        this.multimedia.pause();
    }

    rewindMedia = () => {
        let current_time = this.multimedia.currentTime;
        let new_time = current_time - this.state.time_skip_unit;

        this.multimedia.currentTime = new_time > 0 ? new_time : 0;
    }

    forwardMedia = () => {
        let current_time = this.multimedia.currentTime;
        let new_time = current_time + this.state.time_skip_unit;
        
        this.multimedia.currentTime = new_time > this.state.duration ? this.state.duration : new_time;
    }

    onSeekerChange = (event, value) => {
        this.multimedia.currentTime = value;
    }

    onVolumeChange = (event, value) => {
        this.multimedia.volume = value;
    }

    onPlaybackSpeedChange = (event, value) => {
        this.multimedia.playbackRate = value;
    }

    render() {
        return (
            <Paper
                square
                elevation={ 0 }
                className="p-2 border-top rounded-bottom">
                <audio
                    ref={ ref => this.multimedia = ref }
                    src={ this.props.uri }
                    preload="metadata">
                </audio>
                <Box
                    className="d-flex flex-nowrap ps-3 align-items-center">
                    <Slider
                        className="text-warning"
                        value={ this.state.seeker_time }
                        max={ this.state.duration }
                        onChange={ this.onSeekerChange } />
                    
                    <Box
                        className="d-flex border-right border-2 flex-nowrap p-2 ps-4 m-0 align-items-center">
                        <FormattedDuration
                            duration={ this.state.seeker_time * 1000 } />
                        <Typography
                            className="m-0"
                            variant="overline"
                            display="block"
                            gutterBottom>-</Typography>
                        <FormattedDuration
                            duration={ this.state.duration * 1000 } />
                    </Box>
                </Box>
                <div className="d-flex flex-nowrap">
                <ToggleButtonGroup
                    size="small">
                    <ToggleButton
                        onClick={ this.rewindMedia }
                        value="Rewind"
                        aria-label="rewind">
                        <FastRewind />
                    </ToggleButton>
                    
                    <ToggleButton
                        value="Play"
                        aria-label="play"
                        onClick={ this.toggleMediaPlayback }>
                        { !this.state.is_playing && <PlayArrow /> }
                        { this.state.is_playing && <Pause /> }
                    </ToggleButton>

                    <ToggleButton
                        onClick={ this.forwardMedia }
                        value="Forward"
                        aria-label="forward">
                        <FastForward />
                    </ToggleButton>
                </ToggleButtonGroup>
                
                <div className="flex-fill"></div>

                <ButtonGroup
                    size="small"
                    sx={{
                        '& > *': {
                            color: '#212529',
                            borderColor: '#212529'
                        },
                    }}>                
                    <React.Fragment>
                        <Button
                            ref={ ref => this.playback_speed_button = ref }
                            onClick={ this.togglePlaybackSpeedVisibility }>{ this.state.playback_speed }x</Button>

                        <Popover
                            id="playback_speed_popover"
                            open={ this.state.is_playback_speed_visible }
                            onClose={ this.togglePlaybackSpeedVisibility }
                            anchorEl={ this.playback_speed_button }
                            anchorOrigin={{
                                vertical: 'top',
                                horizontal: 'center'
                            }}
                            transformOrigin={{
                                vertical: 'bottom',
                                horizontal: 'center'
                            }}>
                                <Slider
                                    orientation="vertical"
                                    size="small"
                                    max={ 2 }
                                    step={ 0.1 }
                                    value={ this.state.playback_speed }
                                    onChange={ this.onPlaybackSpeedChange }
                                    sx={{
                                        height: 100,
                                        m: 2
                                    }} />
                        </Popover>
                    </ React.Fragment>
                    
                    <React.Fragment>
                        <Button
                            ref={ ref => this.volume_button = ref }
                            onClick={ this.toggleVolumeVisibility }>
                            <VolumeUp />
                        </Button>

                        <Popover
                            open={ this.state.is_volume_visible }
                            onClose={ this.toggleVolumeVisibility }
                            anchorEl={ this.volume_button }
                            anchorOrigin={{
                                vertical: 'top',
                                horizontal: 'center'
                            }}
                            transformOrigin={{
                                vertical: 'bottom',
                                horizontal: 'center'
                            }}>
                                <Slider
                                    orientation="vertical"
                                    size="small"
                                    max={ 1 }
                                    step={ 0.05 }
                                    value={ this.state.volume }
                                    onChange={ this.onVolumeChange }
                                    sx={{
                                        height: 100,
                                        m: 2
                                    }} />
                        </Popover>
                    </React.Fragment>

                    <Button>
                        <Settings />
                    </Button>
                </ButtonGroup>
                </div>
            </Paper>
        );
    }
}

class FormattedDuration extends React.Component {

    get_format = () => {
        this.format = undefined;

        let seconds = parseInt(this.props.duration / 1000);

        if(seconds >= 3600) {
            this.format = 'H:mm:ss';
        } else {
            this.format = 'mm:ss';
        }

        return this.format;
    }

    render() {
        return (
            <Typography
                className="m-0"
                variant="overline"
                display="block"
                gutterBottom>{ Duration.fromMillis(this.props.duration).toFormat(this.get_format())}</Typography>
        )
    }
}
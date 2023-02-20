import React from 'react';

import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Container from '@mui/material/Container';

import Typography from '@mui/material/Typography';

import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';

import Menu from '@mui/material/Menu';
import MenuList from '@mui/material/MenuList';
import MenuItem from '@mui/material/MenuItem';

import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';

import Search from '@mui/icons-material/Search';
import FindReplace from '@mui/icons-material/FindReplace';
import EditOff from '@mui/icons-material/EditOff';

import Divider from '@mui/material/Divider';

import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';

import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';

import MenuIcon from '@mui/icons-material/Menu';
import Save from '@mui/icons-material/Save';
import Send from '@mui/icons-material/Send';
import Report from '@mui/icons-material/Report';
import MoreVert from '@mui/icons-material/MoreVert';
import Restore from '@mui/icons-material/Restore';
import Update from '@mui/icons-material/Update';
import Shortcut from '@mui/icons-material/Shortcut';
import ListIcon from '@mui/icons-material/List';
import Help from '@mui/icons-material/Help';

import MultimediaPlayer from './MultimediaPlayer';
import { List } from '@mui/material';


export default class TranscriptEditor extends React.Component {
    constructor(props) {
        super(props);
        
        this.menu_toggle_button = undefined;

        this.state = {
            is_menu_open: false,
            is_sidebar_open: false
        };
    }

    toggleMenuVisibility = () => {
        this.setState({
            is_menu_open: !this.state.is_menu_open
        });
    }

    toggleSidebar = () => {
        this.setState({
            is_sidebar_open: !this.state.is_sidebar_open
        });
    }

    render() {
        let type = "audio";
        let uri = "samples/sample.mp3";

        return (
            <Box
                className="h-100 w-100 d-flex flex-column">
                <div className="flex-fill d-flex flex-column bg-light flex-nowrap">
                    <AppBar
                        className="bg-dark p-2 m-0"
                        position="static">
                        <Toolbar>
                            <IconButton
                                className="d-lg-none"
                                onClick={ this.toggleSidebar }
                                size="large"
                                edge="start"
                                color="inherit"
                                aria-label="menu"
                                sx={{ mr: 2 }}>
                                <MenuIcon />
                            </IconButton>
                            <img
                                alt="transcritva_logo"
                                height="60px"
                                width="60px"
                                src="/img/transcript-va-logo-alternate-colors.png" />
                            <div className="flex-fill"></div>
                            <Button
                                className="bg-warning text-dark me-2"
                                endIcon={ <Send /> }
                                variant="contained">Submit</Button>
                            <Button
                                endIcon={ < Report />}
                                className="bg-danger text-white"
                                variant="contained">Cancel</Button>
                        </Toolbar>
                    </AppBar>
                    
                    <div className="flex-fill row mx-0 p-0">
                        <div className="col-2 d-none d-lg-block shadow p-0 m-0 bg-light">
                            <div className="d-flex flex-column h-100 p-0">
                                <List
                                    className="bg-white p-0">                              
                                    <ListItem
                                        disablePadding>
                                        <ListItemButton
                                            className="border-bottom py-3">
                                            <ListItemIcon><ListIcon /></ListItemIcon>
                                            <ListItemText primary="Transcript Details" />
                                        </ListItemButton>
                                    </ListItem>
                                </List>

                                <div
                                    className="flex-fill p-2">
                                    <Paper
                                        className="mx-auto h-100 p-2">
                                        <p class="lead">Details for the transcript</p>
                                    </Paper>
                                </div>
                                <List
                                    className="bg-white mt-auto border-top p-0">
                                    <ListItem
                                        disablePadding>
                                        <ListItemButton
                                            className="border-bottom py-3">
                                            <ListItemIcon><Help /></ListItemIcon>
                                            <ListItemText primary="Contact Support" />
                                        </ListItemButton>
                                    </ListItem>
                                </List>
                            </div>
                        </div>
                        <div className="col-12 col-lg-10 col-sm-10">
                            <Container
                                maxWidth="md"
                                className="mx-auto p-0 position-relative h-100">
                                <div 
                                    className="position-absolute h-100 p-2 mx-auto">
                                    <Paper
                                        className="p-0 position-relative m-0 h-100 w-100">
                                        <div
                                            className="position-absolute rounded-top w-100">
                                            <div
                                                className="border-bottom rounded-top bg-white w-100 p-2">
                                                <div className="d-flex flex-nowrap">
                                                    <div className="flex-fill d-flex border-end me-2 align-items-center justify-content-center">
                                                        <small
                                                            className="text-break">[ this/is/the/file_name_adsf7asdfadfsdfs.mp3 ]</small>
                                                        </div>
                                                    <Button
                                                        className="bg-warning text-dark"
                                                        variant="contained"
                                                        size="small"
                                                        endIcon={ <Save /> }><span className="d-block pt-1">Save</span></Button>
                                                    <IconButton
                                                        onClick={ this.toggleMenuVisibility }
                                                        ref={ ref => { this.menu_toggle_button = ref } }
                                                        aria-label="menu"
                                                        color="inherit"><MoreVert /></IconButton>
                                                    <Menu
                                                        id="basic-menu"
                                                        anchorEl={ this.menu_toggle_button }
                                                        open={ this.state.is_menu_open }
                                                        onClose={ this.toggleMenuVisibility }
                                                        MenuListProps={{
                                                            'aria-labelledby': 'basic-button',
                                                        }}>
                                                        <MenuList
                                                            dense>
                                                            <MenuItem onClick={ this.toggleMenuVisibility }>
                                                                <ListItemIcon>
                                                                    <Restore />
                                                                </ListItemIcon>
                                                                <ListItemText>Undo</ListItemText>
                                                                <Typography
                                                                    className="ms-2 border-left"
                                                                    variant="body2"
                                                                    color="text.secondary">
                                                                    ⌘Z
                                                                </Typography>
                                                            </MenuItem>
                                                            <MenuItem onClick={ this.toggleMenuVisibility }>
                                                                <ListItemIcon>
                                                                    <Update />
                                                                </ListItemIcon>
                                                                <ListItemText>Redo</ListItemText>
                                                                <Typography variant="body2" color="text.secondary">
                                                                    ⌘Y
                                                                </Typography>
                                                            </MenuItem>
                                                            <Divider />
                                                            <MenuItem onClick={ this.toggleMenuVisibility }>
                                                                <ListItemIcon>
                                                                    <Search fontSize="small" />
                                                                </ListItemIcon>
                                                                <ListItemText>Find</ListItemText>
                                                                <Typography variant="body2" color="text.secondary">
                                                                    ⌘F
                                                                </Typography>
                                                            </MenuItem>
                                                            <MenuItem onClick={ this.toggleMenuVisibility }>
                                                                <ListItemIcon>
                                                                    <FindReplace fontSize="small" />
                                                                </ListItemIcon>
                                                                <ListItemText>Find & Replace</ListItemText>
                                                                <Typography
                                                                    className="ms-2 border-left"
                                                                    variant="body2"
                                                                    color="text.secondary">
                                                                    ⌘H
                                                                </Typography>
                                                            </MenuItem>
                                                            <Divider />
                                                            <MenuItem onClick={ this.toggleMenuVisibility }>
                                                                <ListItemIcon>
                                                                    <EditOff fontSize="small" />
                                                                </ListItemIcon>
                                                                <ListItemText>Stop Editing</ListItemText>
                                                                <Typography variant="body2" color="text.secondary">
                                                                    ⌘E
                                                                </Typography>
                                                            </MenuItem>
                                                            <Divider />
                                                            <MenuItem onClick={ this.toggleMenuVisibility }>
                                                                <ListItemIcon>
                                                                    <Shortcut fontSize="small" />
                                                                </ListItemIcon>
                                                                <ListItemText>Configure Shortcuts</ListItemText>
                                                            </MenuItem>
                                                        </MenuList>
                                                    </Menu>
                                                </div>
                                            </div>
                                        </div>
                                        <Box
                                            className="p-3 pt-5 m-0 overflow-auto h-100"
                                            sx={{
                                                overflowY: "auto",
                                                margin: 0,
                                                padding: 0,
                                                listStyle: "none",
                                                height: "100%",
                                                '&::-webkit-scrollbar': {
                                                    width: '0.4em'
                                                },
                                                '&::-webkit-scrollbar-track': {
                                                    boxShadow: 'inset 0 0 6px rgba(0,0,0,0.00)',
                                                    webkitBoxShadow: 'inset 0 0 6px rgba(0,0,0,0.00)',
                                                    backgroundColor: 'rgba(200, 200, 0, 0.1)'
                                                },
                                                '&::-webkit-scrollbar-thumb': {
                                                    backgroundColor: 'rgba(255,193,7,0.5)',
                                                    borderRadius: '10px'
                                                }                                  
                                            }}>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                            <p className="text-break">Lorem ipsum adfasdfa;sdfjkasdffljasskdfjasdf;hasdffhajsdhfahsdfjhajkshdfkjhasdjfkhajskdhfjkashdflkhasdfhaksdfhakhdfjkahsdfkhalkfdhkasdhfjashdflkhaksdhfkjashdf</p>
                                        </Box>
                                    </Paper>
                                </div>
                            </Container>
                        </div>
                    </div>

                    <MultimediaPlayer
                        type={ type }
                        uri={ uri } />    
                </div>
            </Box>
        );
    }
}
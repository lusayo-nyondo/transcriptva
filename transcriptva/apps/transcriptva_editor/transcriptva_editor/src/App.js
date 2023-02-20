import 'bootstrap/dist/css/bootstrap.min.css';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import TranscriptEditor from './components/TranscriptEditor';

import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';

function App() {
  return (
    <Box
      className="w-100 vh-100 p-2">
      <Paper
        elevation={3}
        className='w-100 h-100'>
        <TranscriptEditor />
      </Paper>
    </Box>
  );
}

export default App;

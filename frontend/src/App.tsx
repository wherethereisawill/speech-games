import { Routes, Route } from 'react-router'
import LandingPage from '@/pages/LandingPage'
import BrowseGames from '@/pages/BrowseGames'
import SoundStories from '@/games/SoundStories'
import WhQuestions from '@/games/WhQuestions'
import Settings from '@/pages/Settings'

function App() {

  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/browse" element={<BrowseGames />} />
      <Route path="/settings" element={<Settings />} />
      <Route path="/games/sound-stories" element={<SoundStories />} />
      <Route path="/games/wh-questions" element={<WhQuestions />} />
    </Routes>
  )
}

export default App
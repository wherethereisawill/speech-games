import { Routes, Route } from 'react-router'
import LandingPage from '@/pages/LandingPage'
import BrowseGames from '@/pages/BrowseGames'
import SoundStories from '@/games/SoundStories'

function App() {

  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/browse" element={<BrowseGames />} />
      <Route path="/games/sound-stories" element={<SoundStories />} />
    </Routes>
  )
}

export default App